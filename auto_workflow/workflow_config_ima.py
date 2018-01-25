#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'ima'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.imamuseum.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'IMA-Actors',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'IMA-Actors-model.ttl',
        'input_file': 'IMA-Actors-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Actors'
    },
    {
        'path': repo_path,
        'name': 'IMA-Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'IMA-Objects-model.ttl',
        'input_file': 'IMA-Objects-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Objects',
        'csv_to_jl': True,
        'num_partitions': 20
    },
    {
        'path': repo_path,
        'name': 'IMA-Objects-Dimensions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'IMA-Objects-Dimensions-model.ttl',
        'input_file': 'IMA-Objects-Dimensions-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Objects-Dimensions'
    },
    {
        'path': repo_path,
        'name': 'IMA-Objects-Creation-Location',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'IMA-Objects-Creation-Location-model.ttl',
        'input_file': 'IMA-Objects-Creation-Location-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Objects-Creation-Location'
    },
    {
        'path': repo_path,
        'name': 'IMA-Object-Types-AAT',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E55_Type1',
        'context_uri': context_uri,
        'model_file': 'IMA-Object-Types-AAT-model.ttl',
        'input_file': 'IMA-Object-Types-AAT-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Object-Types-AAT'
    },
    {
        'path': repo_path,
        'name': 'IMA-Technique-AAT',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E55_Type1',
        'context_uri': context_uri,
        'model_file': 'IMA-Technique-AAT-model.ttl',
        'input_file': 'IMA-Technique-AAT-data.csv',
        'input_file_type': 'csv',
        'output_file_name': 'IMA-Technique-AAT'
    },
    {
       'path': repo_path,
       'name': 'IMA_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'IMA_Metadata-model.ttl',
       'input_file': 'IMA_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'IMA_Metadata'
    }
]
