#!/usr/bin/env python

from sys import argv

from py4j.java_gateway import java_import

from pyspark import SparkContext
from digWorkflow.workflow import Workflow


'''
This sample loads CSV data, applies karma model on the CSV data and as a sample, outputs n3.
You can change karma.output.format to json to output json.

If the workflow gives Out of memory error, you can increase the numPartitions to increase parallelism.

Executed as:


spark-submit \
      --archives ~/github/aac-alignment/karma.zip \
      --py-files ../lib/python-lib.zip \
      --driver-class-path ~/github/Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar \
      karmaWorkflowCSV.py ~/Downloads/LOD-CBMAA-Constituents.csv ~/Downloads/LOD-N3

'''

if __name__ == "__main__":
    sc = SparkContext(appName="karmaCSV")

    java_import(sc._jvm, "edu.isi.karma")

    inputFilename = argv[1]
    outputFilename = argv[2]
    numPartitions = 1

    workflow = Workflow(sc)

    #1. Read the input
    inputRDD = workflow.batch_read_csv(inputFilename)

    #2. Apply the karma Model
    outputRDD = workflow.run_karma(inputRDD,
                                   "https://raw.githubusercontent.com/american-art/cbm/master/CBMAA_Roles/CBMAA_Roles-model.ttl",
                                   "http://americanart.isi.edu/data/",
                                   "http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1",
                                   "https://raw.githubusercontent.com/dkapoor/test/master/sample-unicode-context.json",
                                   num_partitions=numPartitions,
                                   data_type="csv",
                                   additional_settings={"karma.input.delimiter":",", "karma.output.format": "n3"})


    #3. Save the output
    outputRDD.map(lambda x: x[1]).saveAsTextFile(outputFilename)

