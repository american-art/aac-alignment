#!/usr/bin/env python

import os, sys
import logging
import requests
import base64
import colorer
import zipfile
from itertools import islice

# config
from config import *

# global variables
req = requests.session()
req.headers.update({'User-Agent': 'USC-ISI'})

logging.basicConfig(
    stream = sys.stdout,
    level = LOG_LEVEL,
    format = '%(asctime)s [%(levelname)s] %(message)s',
    datefmt = '%d %b %Y %H:%M:%S'
)

def http_error_format(resp):
    return 'status_code: ' + str(resp.status_code) + \
           '\n headers: ' + str(resp.headers) + \
           '\n content: ' + resp.content

def import_data(data, dataset, graph = 'default'):
    url = '%s/%s/data?graph=%s' % (FUSEKI_URL, dataset, graph)
    files = {
        'file': ('file.n3', data, 'application/octet-stream')
    }
    headers = {}
    if FUSEKI_ACCOUNT != None:
        headers['Authorization'] = 'Basic ' + base64.b64encode(FUSEKI_ACCOUNT[0] + ':' + FUSEKI_ACCOUNT[1])
    try:
        resp = req.post(url = url, files = files, headers = headers, timeout = NETWORK_TIMEOUT)
        if resp.status_code // 100 != 2:
            logging.error(http_error_format(resp))
        logging.info('imported into graph : ' + graph)

    except Exception as e:
        logging.error(str(e))

def drop_graph(dataset, graph):
    url = '%s/%s/update' % (FUSEKI_URL, dataset)
    data = {}
    data['update'] = 'drop graph<%s%s>' % (GRAPH_BASE_URL, graph)

    logging.info('drop graph: ' + GRAPH_BASE_URL + graph)
    headers = {}
    if FUSEKI_ACCOUNT != None:
        headers['Authorization'] = 'Basic ' + base64.b64encode(FUSEKI_ACCOUNT[0] + ':' + FUSEKI_ACCOUNT[1])
    try:
        resp = req.post(url = url, data = data, headers = headers, timeout = NETWORK_TIMEOUT)
        if resp.status_code // 100 != 2:
            logging.error('drop graph: [%d]' % resp.status_code)
            return
    except Exception as e:
        logging.error(str(e))

def zip_extract(zip_file, output):
    try:
        zip_obj = zipfile.ZipFile(zip_file)
        zip_obj.extractall(output)
    except:
        logging.error('zip read: ' + zip_file)


if __name__ == '__main__':

    # python auto_import.py [repo_name] [dev|pro]

    repo = sys.argv[1]
    dataset = TDB_DATASET_NAME if sys.argv[2] == 'pro' else TDB_DEV_DATASET_NAME
    if repo not in REPOS:
        logging.error('invalid museum')
        sys.exit()

    logging.info('Dataset: ' + dataset)
    logging.info('Start to process repo: ' + repo)

    abs_path = os.path.abspath(DIR_PATH)
    abs_path = os.path.join(abs_path, repo)

    # Drop both the graphs of a museum, default and curated
    drop_graph(dataset, repo)
    drop_graph(dataset, "curated_"+repo)
    
    for dir_name in os.listdir(abs_path):
        # ignore IGNORE_DIRS and non-dir files
        curr_dir = os.path.join(abs_path, dir_name)
        if dir_name in IGNORE_DIRS or not os.path.isdir(curr_dir):
            continue

        logging.info('process on directory: ' + curr_dir)
        output = os.path.join(curr_dir, OUTPUT_DIR)

        # unzip .n3.zip file to output dir and import unzipped .n3 file to tdb
        for n3_name in os.listdir(curr_dir):
            # Ignore n3.zip from curated folder
            if n3_name.endswith('.n3.zip'):
                zip_file = os.path.join(curr_dir, n3_name)
                zip_extract(zip_file, output)

        # Read all n3 file and load its data into triple store
        if os.path.isdir(output):
            for o_name in os.listdir(output):
                file = os.path.join(output, o_name)
                if os.path.isfile(file) and o_name.endswith('.n3'):
                    logging.info('importing data file : ' + o_name)
                    
                    chunk_size = 100000 # read 100k lines everytime
                    with open(file, 'r') as f:
                        while True:
                            next_chunk = ''.join(list(islice(f, chunk_size)))
                            if not next_chunk:
                                break

                            # n3 file containing curated results go to "curated" graph
                            if 'curated.n3' in o_name:
                                # Data -> actual data, dataset -> american-art/dev, graph-> "/curated"
                                import_data(next_chunk, dataset, GRAPH_BASE_URL + "curated_" + repo)
                            else:
                                import_data(next_chunk, dataset, GRAPH_BASE_URL + repo)
