#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.sql.functions import explode
from py4j.java_gateway import java_import
from digWorkflow.workflow import Workflow
from digSparkUtil.fileUtil import FileUtil

import json
import sys, os
import logging
import urlparse, urllib
import shutil
import time
import zipfile
from importlib import import_module
# import workflow_config

logging.basicConfig(
    stream = sys.stdout,
	format = '%(asctime)s [%(levelname)s] %(message)s',
	datefmt = '%d %b %Y %H:%M:%S'
)

def init_repo_config(config):
    # fill variables
    name = config['name']
    if 'input_file' not in config:
        config['input_file'] = name + '.csv'
    if 'input_file_type' not in config:
        config['input_file_type'] = 'csv'
    if 'output_dir' not in config:
        config['output_dir'] = 'output'
    if 'output_file_name' not in config:
        config['output_file_name'] = name
    if 'output_file_type' not in config:
        config['output_file_type'] = 'n3'
    if 'model_file' not in config:
        config['model_file'] = name + '-model.ttl'
    if 'num_partitions' not in config:
        config['num_partitions'] = 1
    if 'additional_settings' not in config:
        config['additional_settings'] = {}

    # add settings
    if config['input_file_type'] == 'csv' and 'karma.input.delimiter' not in config['additional_settings']:
        config['additional_settings']['karma.input.delimiter'] = ','
    if config['output_file_type'] == 'n3' and 'karma.output.format' not in config['additional_settings']:
        config['additional_settings']['karma.output.format'] = 'n3'

    # construct path
    abs_path = os.path.abspath(config['path'])
    abs_path = os.path.join(abs_path, config['name'])
    config['input_file'] = os.path.join(abs_path, config['input_file'])
    config['output_dir'] = os.path.join(abs_path, config['output_dir'])
    config['output_file'] = os.path.join(abs_path, config['output_file_name'] + '.' + config['output_file_type'])
    config['model_file'] = os.path.join(abs_path, config['model_file'])

    # model file to uri
    if 'model_uri' not in config:
        config['model_uri'] =  urlparse.urljoin('file:', urllib.pathname2url(config['model_file']))

    # clean up output folder
    output_dir = os.path.join(config['output_dir'])
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        time.sleep(1)

def concatenate_output(output_file, output_dir):
    success_file = os.path.join(output_dir, '_SUCCESS')
    if not os.path.exists(success_file):
        logging.error('no _SUCCESS file in ' + output_dir)
        return

    with open(output_file, 'w') as outfile:
        for name in os.listdir(output_dir):
            file = os.path.join(output_dir, name)
            if os.path.isfile(file) and name.startswith('part-'):
                with open(file) as infile:
                    for line in infile:
                        outfile.write(line)

def zip_file(file, delete_after_zip = False):
    with zipfile.ZipFile(file + '.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
        zip.write(file, os.path.basename(file))
    if delete_after_zip:
        os.remove(file)

if __name__ == '__main__':

    # get config file
    config_module = import_module(sys.argv[1])
    logging.basicConfig(level = config_module.LOG_LEVEL)

    # init spark and jvm
    sc = SparkContext(appName = 'Auto AAC Workflow')
    java_import(sc._jvm, 'edu.isi.karma')

    file_util = FileUtil(sc)
    workflow = Workflow(sc)

    logging.info('Number of model: %d' % len(config_module.REPO_CONFIG))
    for config in config_module.REPO_CONFIG:
        init_repo_config(config)

        # Read the input
        logging.info('read input file: ' + config['input_file'])
        if config['input_file_type'] == 'csv':
            input_rdd = workflow.batch_read_csv(config['input_file'])
        elif config['input_file_type'] == 'json':
            # input_rdd = workflow.read_json_file(config['input_file'])
            input_rdd = sc.wholeTextFiles(config['input_file']).mapValues(lambda x: json.loads(x))
            # print "Load file:", config['input_file']
            #input_rdd = file_util.load_file(config['input_file'], file_format = 'text', data_type = 'json')
            # input_rdd = sc.textFile(config['input_file']).map(lambda x: ("test", json.loads(x)))
        elif config['input_file_type'] == 'xml':
            input_rdd = sc.wholeTextFiles(config['input_file'])
        elif config['input_file_type'] == 'jsonlines':
            config['input_file_type'] = "json"
            input_rdd = sc.textFile(config['input_file']).map(lambda x: ("test", json.loads(x)))
            #input_rdd = workflow.read_json_file(config['input_file'])

        # Apply the karma Model
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

        # Save the output
        # output_rdd.values().saveAsTextFile(config['output_file'])
        output_rdd.values().distinct().saveAsTextFile(config['output_dir'])

        # # concatenate to a single file and zip it
        concatenate_output(config['output_file'], config['output_dir'])
        zip_file(config['output_file'], True)
