#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.sql.functions import explode
from py4j.java_gateway import java_import
from workflow import Workflow
from sys import argv
import json
import sys
from digSparkUtil.fileUtil import FileUtil

'''
rm -rf karma-out-autry; spark-submit \
      --archives karma.zip \
      --py-files lib/python-lib.zip \
      --driver-class-path .../Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar \
      AutryWorkflowCSV.py AutryMakers.csv karma-out-autry
'''

def mapFunc(x): 
        f_dict  = {}
        f_dict["@id"] = x['uri']
        f_dict["@type"] = "http://schema.org/Person"
        try:
            if type(x['P131_is_identified_by']) is list:
                f_dict["schema:name"] = x['P131_is_identified_by'][0]['label']
            elif type(x['P131_is_identified_by']) is dict:
                f_dict["schema:name"] = x['P131_is_identified_by']['label']
        except KeyError:
            pass
        return f_dict

if __name__ == "__main__":
    
    sc = SparkContext(appName="TEST")

    java_import(sc._jvm, "edu.isi.karma")

    inputFilename = argv[1]
    outputFilename = argv[2]

    numPartitions = 1
    numFramerPartitions = max(10, numPartitions / 10)

    fileUtil = FileUtil(sc)
    workflow = Workflow(sc)
    contextUrl = "https://raw.githubusercontent.com/american-art/aac-alignment/master/karma-context.json"

    #1. Read the input
    inputRDD = workflow.batch_read_csv(inputFilename)

    #2. Apply the karma Model
    outputRDD = workflow.run_karma(inputRDD,
                                   "https://raw.githubusercontent.com/american-art/autry/master/AutryMakers/AutryMakers-model.ttl",
                                   "http://americanartcollaborative.org/autry/",
                                   "http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1",
                                   "https://raw.githubusercontent.com/american-art/aac-alignment/master/karma-context.json",
                                   num_partitions=numPartitions,
                                   data_type="csv",
                                   additional_settings={"karma.input.delimiter":","})

    #3. Save the output
    # fileUtil.save_file(outputRDD, outputFilename, "text", "json")

    #4. Reduce rdds
    reducedRDD = workflow.reduce_rdds(numFramerPartitions, outputRDD)
    reducedRDD.persist()

    types = [
        {"name": "E39_Actor", "uri": "http://www.cidoc-crm.org/cidoc-crm/E39_Actor"},
        {"name": "E82_Actor_Appellation", "uri": "http://www.cidoc-crm.org/cidoc-crm/E82_Actor_Appellation"}
    ]
    frames = [
        {"name": "AutryMakers", "url": "https://raw.githubusercontent.com/american-art/aac-alignment/master/frames/autryMakers.json-ld"}
    ]

    type_to_rdd_json = workflow.apply_partition_on_types(reducedRDD, types)

    #4. Apply Framer
    framer_output = workflow.apply_framer(reducedRDD, type_to_rdd_json, frames, numFramerPartitions, 10)

    for frame_name in framer_output:
        #5. Map function
        framer_output[frame_name] = framer_output[frame_name].mapValues(mapFunc)
        fileUtil.save_file(framer_output[frame_name], outputFilename + "/" + frame_name, 'text', 'json')
        print "Save to:", ("---" + frame_name)
