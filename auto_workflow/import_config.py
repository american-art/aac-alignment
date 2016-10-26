#!/usr/bin/env python
import logging

DIR_PATH = './../../aac-repos/'
REPOS = [
	# 'autry',
	'npg',
]
IGNORE_DIRS = ['.git']
OUTPUT_DIR = 'output'

# tdb should set `tdb:unionDefaultGraph true`
FUSEKI_URL = 'http://localhost:3030'
GRAPH_BASE_URL = 'http://data.americanartcollaborative.org/'
# FUSEKI_ACCOUNT = ('', '')
TDB_DATASET_NAME = 'american-art'
FUSEKI_ACCOUNT = None
FUSEKI_FORCE_OVERWRITE = True # delete the data store which has the same name before import
LOG_LEVEL = logging.INFO
NETWORK_TIMEOUT = None