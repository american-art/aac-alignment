#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'ccma'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.museum.colby.edu/aac/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'ccma_artists',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'ccma_artists-model.ttl',
        'input_file': 'ccma_artists.json',
        'input_file_type': 'json',
        'output_file_name': 'ccma_artists'
    },
    {
        'path': repo_path,
        'name': 'ccma_objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'ccma_objects-model.ttl',
        'input_file': 'ccma_objects.json',
        'input_file_type': 'json',
        'output_file_name': 'ccma_objects'
    },
    {
       'path': repo_path,
       'name': 'CCMA_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription/DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'CCMA_Metadata-model.ttl',
       'input_file': 'CCMA_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'CCMA_Metadata'
    }
]
