#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'ima'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/ima/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'aac-actors',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'aac-actors-model.ttl',
        'input_file': 'aac-actors.json',
        'input_file_type': 'json',
        'output_file_name': 'aac-actors'
    },
    #{
    #    'path': repo_path,
    #    'name': 'aac-objects',
    #    'base_uri': base_uri,
    #    'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #    'context_uri': context_uri,
    #    'model_file': 'aac-objects-model.ttl',
    #    'input_file': 'aac-objects_folded.json',
    #    'input_file_type': 'json',
    #    'output_file_name': 'aac-objects'
    #},
]
