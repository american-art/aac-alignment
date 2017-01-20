#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'dma'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/dma/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'DMA_Constituents-model.ttl',
        'input_file': 'Dallas Museum of Art - LOD - UPDATED.csv',
        'input_file_type': 'csv',
        'output_file_name': 'DMA_Constituents-model'
    },
    {
        'path': repo_path,
        'name': 'Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'DMA-model.ttl',
        'input_file': 'Dallas Museum of Art - LOD - UPDATED.csv',
        'input_file_type': 'csv',
        'output_file_name': 'DMA-model'
    },
]