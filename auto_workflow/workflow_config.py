#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
REPO_CONFIG = [
    # {
    #     'path': './../../',
    #     'repo': 'autry',
    #     'name': 'AutryMakers',
    #     'input_file': 'AutryMakers.csv', # optional
    #     'input_file_type': 'csv', # optional
    #     'output_dir': 'output', # optional
    #     'output_file_type': 'n3', # optional
    #     # 'model_uri': '', # model_uri or model_file
    #     'model_file': 'AutryMakers.ttl',
    #     'base_uri': 'http://americanartcollaborative.org/autry/',
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json',
    #     'num_partitions': 3, # optional
    #     'additional_settings': {} # optional
    # },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryCultureMade',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryDated',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryMakers',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryMedia',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryObjects',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryPubDesc',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    },
    {
        'path': './../../',
        'repo': 'autry',
        'name': 'AutryPublications',
        'base_uri': 'http://americanartcollaborative.org/autry/',
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
    }
]