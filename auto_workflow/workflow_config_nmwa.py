#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'nmwa'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.wildlifeart.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'Data',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NMWA_Data-model.ttl',
        'input_file': 'NMWA_Data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NMWA_Data'
    },
    {
        'path': repo_path,
        'name': 'Classifications',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E57_Material1',
        'context_uri': context_uri,
        'model_file': 'Classifications-model.ttl',
        'input_file': 'Classifications.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Classifications'
    },
    {
        'path': repo_path,
        'name': 'Actor',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'NMWA_Actor-model.ttl',
        'input_file': 'NMWA_Data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Actor'
    },
    {
       'path': repo_path,
       'name': 'NMWA_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription/DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'NMWA_Metadata-model.ttl',
       'input_file': 'NMWA_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'NMWA_Metadata'
    }
]
