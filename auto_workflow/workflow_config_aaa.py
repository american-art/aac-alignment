#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'aaa'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/aaa/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
       'path': repo_path,
       'name': 'Item_People',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_People-model.ttl',
       'input_file': 'Item_People.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_People'
    },
    {
       'path': repo_path,
       'name': 'Item_Institutions',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_Institutions-model.ttl',
       'input_file': 'Item_Institutions.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_Institutions'
    },
]
  