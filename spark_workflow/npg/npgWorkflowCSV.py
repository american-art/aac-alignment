from pyspark import SparkContext
from pyspark.sql.functions import explode
from py4j.java_gateway import java_import
from workflow import Workflow
from sys import argv
import json
import sys
from digSparkUtil.fileUtil import FileUtil

'''
rm -rf karma-out-npg; spark-submit \
      --archives karma.zip \
      --py-files lib/python-lib.zip \
      --driver-class-path .../Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar \
      npgWorkflowCSV.py NPGConstituents.csv karma-out-npg

'''

def mapFunc(x): 
    f_dict  = {}
    firstname = lastname =  middlename = name_string = ""
    nameList = []
    f_dict["@id"] = x['uri']
    f_dict["@type"] = "http://schema.org/Person"

    try:
        f_dict["schema:birthDate"] = int(x['P98i_was_born']['P4_has_time-span']['P82_at_some_time_within'])
    except KeyError:
        pass

    try:
        f_dict["schema:deathDate"] = int(x['P100i_died_in']['P4_has_time-span']['P82_at_some_time_within'])
    except KeyError:
        pass

    try:
        if type(x['P131_is_identified_by']['P106_is_composed_of']) is dict:
            nameList.append(x['P131_is_identified_by']['P106_is_composed_of'])
        elif type(x['P131_is_identified_by']['P106_is_composed_of']) is list:
            nameList = x['P131_is_identified_by']['P106_is_composed_of']
        for sub_name in nameList:
            tag = sub_name['uri'].rsplit("/", 1)
            if tag[1] == "firstname":
                firstname = sub_name['label']
            elif tag[1] == "lastname":
                lastname = sub_name['label']
            elif tag[1] == "middlename":
                middlename = sub_name['label']
        name_string += lastname
        if firstname != "" :
            name_string += ", " + firstname
        if middlename != "" :
            name_string += " " + middlename
        f_dict["schema:name"] = name_string
    except KeyError:
        pass

    return f_dict

if __name__ == "__main__":

    sc = SparkContext(appName="TEST")

    java_import(sc._jvm, "edu.isi.karma")

    inputFilename = argv[1]
    outputFilename = argv[2]
    numPartitions = 1000
    numFramerPartitions = max(10, numPartitions / 10)

    fileUtil = FileUtil(sc)
    workflow = Workflow(sc)
    contextUrl = "https://raw.githubusercontent.com/american-art/aac-alignment/master/karma-context.json"

    #1. Read the input
    inputRDD = workflow.batch_read_csv(inputFilename)

    #2. Apply the karma Model
    outputRDD = workflow.run_karma(inputRDD,
                                   "https://raw.githubusercontent.com/american-art/npg/master/NPGConstituents/NPGConstituents-model.ttl",
                                   "http://americanartcollaborative.org/npg/",
                                   "http://www.cidoc-crm.org/cidoc-crm/E39_Actor1",
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
        {"name": "E82_Actor_Appellation", "uri": "http://www.cidoc-crm.org/cidoc-crm/E82_Actor_Appellation"},
        {"name": "E67_Birth", "uri": "http://www.cidoc-crm.org/cidoc-crm/E67_Birth"},
        {"name": "E69_Death", "uri": "http://www.cidoc-crm.org/cidoc-crm/E69_Death"},
        {"name": "E52_Time-Span", "uri": "http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span"}
    ]
    frames = [
        {"name": "npgConstituents", "url": "https://raw.githubusercontent.com/american-art/aac-alignment/master/frames/npgConsitituents.json-ld"}
    ]

    type_to_rdd_json = workflow.apply_partition_on_types(reducedRDD, types)

    #5. Apply framer
    framer_output = workflow.apply_framer(reducedRDD, type_to_rdd_json, frames, numFramerPartitions, 10)

    for frame_name in framer_output:
        #6. Map function
        framer_output[frame_name] = framer_output[frame_name].mapValues(mapFunc)
        fileUtil.save_file(framer_output[frame_name], outputFilename + "/" + frame_name, 'text', 'json')
        print "Save to:", ("---" + frame_name)

