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

def drop_graph(dataset, graphbaseurl, graph):

    url = '%s/%s/update' % (graphbaseurl, dataset)
    data = {}
    data['update'] = 'drop graph<%s/%s/%s>' % (graphbaseurl, dataset, graph)
    logging.info('drop graph: ',data['update'])
    
    try:
        resp = req.post(url = url, data = data, headers = {}, timeout = NETWORK_TIMEOUT)
        if resp.status_code // 100 != 2:
            logging.error('drop graph: [%d]' % resp.status_code)
            return
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':

    # python drop_customgraph.py [dev|pro] [graph_baseurl] [graph_name] 
    # Below are two example of the graph URL
    # FUSEKI_URL = 'http://localhost:3030/'
    # GRAPH_BASE_URL = 'http://data.americanartcollaborative.org/'
    
    if len(sys.argv) != 4:
        logging.error('invalid arguments')
        looging.error('Usage: python drop_customgraph.py [dev|pro] [graph_baseurl] [graph_name]')
        sys.exit()
    
    dataset = TDB_DATASET_NAME if sys.argv[1] == 'pro' else TDB_DEV_DATASET_NAME
    graph = sys.argv[2]
    graphbaseurl = sys.argv[3]
    
    logging.info('Dropping Graph '+graphbaseurl+dataset+'/'+graph)
    drop_graph(dataset, graphbaseurl, graph)
