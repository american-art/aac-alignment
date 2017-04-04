#!/usr/bin/env python

import os, sys, shutil
import logging
import requests
import base64

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

def drop_graph(dataset, graph):

    url = '%s/%s/update' % (FUSEKI_URL, dataset)
    data = {}
    data['update'] = 'drop graph<%s/%s/%s>' % (FUSEKI_URL, dataset, graph)
    logging.info('drop graph: ',data['update'])
    
    try:
        resp = req.post(url = url, data = data, headers = {}, timeout = NETWORK_TIMEOUT)
        if resp.status_code // 100 != 2:
            logging.error('drop graph: [%d]' % resp.status_code)
            return
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':

    # python drop_graph.py [dev|pro] [graph_name] 
    graph = sys.argv[2]
    dataset = TDB_DATASET_NAME if sys.argv[1] == 'pro' else TDB_DEV_DATASET_NAME
    if graph in REPOS:
        logging.info('Removing Graph '+graph+' from dataset '+dataset)
        drop_graph(dataset, graph)
    elif graph == ".":
        for g in REPOS:
            logging.info('Removing Graph '+g+' from dataset '+dataset)
            drop_graph(dataset, g)
    else:
        logging.error('invalid museum')
        sys.exit()



