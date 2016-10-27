#!/usr/bin/env python

import os, sys
import logging
import requests
import base64
import colorer
import zipfile

# config
from import_config import *

# global variables
req = requests.session()
req.headers.update({'User-Agent': 'USC-ISI'})

logging.basicConfig(
    level = LOG_LEVEL,
    format = '%(asctime)s [%(levelname)s] %(message)s',
    datefmt = '%d %b %Y %H:%M:%S'
)

def import_data(data, graph = 'default'):
    url = '%s/%s/data?graph=%s' % (FUSEKI_URL, TDB_DATASET_NAME, graph)
    files = {
        'file': ('file.n3', data, 'application/octet-stream')
    }
    logging.info('import data into graph: ' + graph)
    headers = {}
    if FUSEKI_ACCOUNT != None:
        headers['Authorization'] = 'Basic ' + base64.b64encode(FUSEKI_ACCOUNT[0] + ':' + FUSEKI_ACCOUNT[1])
    try:
        resp = req.post(url = url, files = files, headers = headers, timeout = NETWORK_TIMEOUT)
        if resp.status_code != 200:
            logging.error(resp.content)
    except Exception as e:
        logging.error(e)

def drop_graph(graph):
    url = '%s/%s/update' % (FUSEKI_URL, TDB_DATASET_NAME)
    data = {}
    data['update'] = 'drop graph<%s/%s/%s>' % (FUSEKI_URL, TDB_DATASET_NAME, graph)

    logging.info('drop graph: ' + graph)
    headers = {}
    if FUSEKI_ACCOUNT != None:
        headers['Authorization'] = 'Basic ' + base64.b64encode(FUSEKI_ACCOUNT[0] + ':' + FUSEKI_ACCOUNT[1])
    try:
        resp = req.post(url = url, data = data, headers = headers, timeout = NETWORK_TIMEOUT)
        if resp.status_code != 200:
            logging.error('drop graph: [%d]' % resp.status_code)
            return
    except Exception as e:
        logging.error(e)

def zip_extract(zip_file, output):
    try:
        zip_obj = zipfile.ZipFile(zip_file)
        zip_obj.extractall(output)
    except:
        logging.error('zip read: ' + zip_file)


if __name__ == '__main__':

    for repo in REPOS:
        logging.info('Start to process repo: ' + repo)

        abs_path = os.path.abspath(DIR_PATH)
        abs_path = os.path.join(abs_path, repo)

        drop_graph(GRAPH_BASE_URL + repo)
        for name in os.listdir(abs_path):
            # ignore IGNORE_DIRS and non-dir files
            curr_dir = os.path.join(abs_path, name)
            if name in IGNORE_DIRS or not os.path.isdir(curr_dir):
                continue

            logging.info('process on directory: ' + curr_dir)
            # unzip .n3.zip file to output dir and import unzipped .n3 file to tdb
            for name in os.listdir(curr_dir):
                if name.endswith('.n3.zip'):
                    zip_file = os.path.join(curr_dir, name)
                    output = os.path.join(curr_dir, OUTPUT_DIR)
                    zip_extract(zip_file, output)

                    for name in os.listdir(output):
                        file = os.path.join(output, name)
                        if os.path.isfile(file) and name.endswith('.n3'):
                            f = open(file, 'r')
                            data = f.read()
                            f.close()
                            logging.info('import data piece: ' + name)
                            import_data(data, GRAPH_BASE_URL + repo)

            # # check if output is generated success
            # curr_dir = os.path.join(curr_dir, OUTPUT_DIR)
            # success_file = os.path.join(curr_dir, '_SUCCESS')
            # if not os.path.exists(success_file):
            #     logging.error('no _SUCCESS file in ' + curr_dir)
            #     continue
            #
            # for name in os.listdir(curr_dir):
            #     file = os.path.join(curr_dir, name)
            #     if os.path.isfile(file) and name.startswith('part-'):
            #         f = open(file, 'r')
            #         data = f.read()
            #         f.close()
            #         logging.info('import data piece: ' + name)
            #         import_data(data, GRAPH_BASE_URL + repo)


