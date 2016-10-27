#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'autry'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/autry/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    # {
    #     'path': './../../',
    #     'repo': 'autry',
    #     'name': 'AutryMakers',
    #     'input_file': 'AutryMakers.csv', # optional
    #     'input_file_type': 'csv', # optional
    #     'output_dir': 'output', # optional
    #     'output_file_name': 'AutryMarkers', # optional
    #     'output_file_type': 'n3', # optional
    #     # 'model_uri': '', # model_uri or model_file
    #     'model_file': 'AutryMakers.ttl',
    #     'base_uri': 'http://americanartcollaborative.org/autry/',
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json',
    #     'num_partitions': 3, # optional
    #     'additional_settings': {}, # optional
    # },
    {
        'path': repo_path,
        'name': 'AutryCultureMade',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        # 'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E12_Production',
        'context_uri': context_uri
    },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryDated',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryMakers',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryMedia',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryObjects',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryPubDesc',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # },
    # {
    #     'path': repo_path,
    #     'repo': repo_name,
    #     'name': 'AutryPublications',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri
    # }
]