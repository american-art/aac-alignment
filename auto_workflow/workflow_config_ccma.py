#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'ccma'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/ccma/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'ccmadata',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'ccma-museum-model.ttl',
        'input_file': 'ccma-objects_artists_exhibs.json',
        'input_file_type': 'json',
        'output_file_name': 'ccma-museum'
    },
]