#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'wam'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/wam/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    # {
    #     'path': repo_path,
    #     'name': 'NPGBibReferences',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E31_Document1',
    #     'context_uri': context_uri,
    #     'model_file': 'npgbibreferences-model.ttl',
    #     'input_file': 'npgbibreferences.csv',
    #     'output_file_name': 'npgbibreferences'
    # },
]