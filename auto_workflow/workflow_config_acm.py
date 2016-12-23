#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'acm'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/acm/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
   {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist'
   },
   {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects'
   },
]
  