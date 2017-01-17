#!/usr/bin/env python
import logging

DIR_PATH = './../../aac-repos/'
REPOS = [
    'acm',
    'autry',
    'cbm',
    'ccma',
    'dma',
    'GM',
    'ima',
    'nmwa',
    'npg',
    'puam',
    'wam',
]
IGNORE_DIRS = ['.git']
OUTPUT_DIR = 'output'

# tdb should set `tdb:unionDefaultGraph true`
FUSEKI_URL = 'http://localhost:3030'
GRAPH_BASE_URL = 'http://data.americanartcollaborative.org/'
# FUSEKI_ACCOUNT = ('', '')
FUSEKI_ACCOUNT = None
TDB_DATASET_NAME = 'american-art'
TDB_DEV_DATASET_NAME = 'american-art-dev'
LOG_LEVEL = logging.INFO
NETWORK_TIMEOUT = None

FLASK_SECRET_KEY = 'secret!'
REMOTE_UPDATE_USERS = {
    'admin': '123', # username (same as session token), password
}
WEB_SOCKET_PORT = 5000