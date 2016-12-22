#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'cbm'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.crystalbridges.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'CBMAAConstituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAAConstituents-model.ttl',
        'input_file': 'LOD CBMAA Constituents.csv',
        'output_file_name': 'CBMAAConstituents'
    },
]