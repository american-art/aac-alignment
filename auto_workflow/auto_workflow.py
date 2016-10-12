#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.sql.functions import explode
from py4j.java_gateway import java_import
from digWorkflow.workflow import Workflow
from sys import argv
from digSparkUtil.fileUtil import FileUtil

import json
import sys, os
import logging
import workflow_config
import urlparse, urllib
import shutil
import time

logging.basicConfig(
	level = workflow_config.LOG_LEVEL,
	format = '%(asctime)s [%(levelname)s] %(message)s',
	datefmt = '%d %b %Y %H:%M:%S'
)

'''
  rm -rf karma_out; spark-submit \
  --archives ~/karma.zip \
  --py-files ~/python-lib.zip \
  --driver-class-path ~/Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar \
  auto_workflow.py

'''

def init_repo_config(config):
    # fill variables
    name = config['name']
    if 'input_file' not in config:
        config['input_file'] = name + '.csv'
    if 'input_file_type' not in config:
        config['input_file_type'] = 'csv'
    if 'output_dir' not in config:
        config['output_dir'] = 'output'
    if 'output_file_type' not in config:
        config['output_file_type'] = 'n3'
    if 'model_file' not in config:
        config['model_file'] = name + '.ttl'
    if 'num_partitions' not in config:
        config['num_partitions'] = 100
    if 'additional_settings' not in config:
        config['additional_settings'] = {}

    # add settings
    if config['input_file_type'] == 'csv' and 'karma.input.delimiter' not in config['additional_settings']:
        config['additional_settings']['karma.input.delimiter'] = ','
    if config['output_file_type'] == 'n3' and 'karma.output.format' not in config['additional_settings']:
        config['additional_settings']['karma.output.format'] = 'n3'

    # construct path
    abs_path = os.path.abspath(config['path'])
    abs_path = os.path.join(abs_path, config['repo'])
    abs_path = os.path.join(abs_path, config['name'])
    config['input_file'] = os.path.join(abs_path, config['input_file'])
    config['output_dir'] = os.path.join(abs_path, config['output_dir'])
    config['model_file'] = os.path.join(abs_path, config['model_file'])

    # model file to uri
    if 'model_uri' not in config:
        config['model_uri'] =  urlparse.urljoin('file:', urllib.pathname2url(config['model_file']))

    # clean up output folder
    output_dir = os.path.join(config['output_dir'])
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        time.sleep(1)

if __name__ == '__main__':

    print '--------------------------'

    sc = SparkContext(appName = 'Auto AAC Workflow')
    java_import(sc._jvm, 'edu.isi.karma')

    for config in workflow_config.REPO_CONFIG:
        init_repo_config(config)

        file_util = FileUtil(sc)
        workflow = Workflow(sc)

        #1. Read the input
        if config['input_file_type'] == 'csv':
            logging.info('read input file: ' + config['input_file'])
            input_rdd = workflow.batch_read_csv(config['input_file'])

        #2. Apply the karma Model
        logging.info('apply karma model')
        output_rdd = workflow.run_karma(
            input_rdd,
            config['model_uri'],
            config['base_uri'],
            config['rdf_root_uri'],
            config['context_uri'],
            num_partitions = config['num_partitions'],
            data_type = config['input_file_type'],
            additional_settings = config['additional_settings']
        )

        #3. Save the output
        # output_rdd.values().saveAsTextFile(config['output_file'])
        output_rdd.values().distinct().saveAsTextFile(config['output_dir'])