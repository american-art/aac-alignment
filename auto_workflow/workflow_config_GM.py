#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'GM'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/GM/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'Attributes',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Attributes-model.ttl',
        'input_file': 'Attributes.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Attributes'
    },
    {
        'path': repo_path,
        'name': 'Classifications',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Classifications-model.ttl',
        'input_file': 'Classifications.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Classifications'
    },
    {
        'path': repo_path,
        'name': 'Constituents_institutions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'Constituents_institutions-model.ttl',
        'input_file': 'Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Constituents_institutions'
    },
    {
        'path': repo_path,
        'name': 'Constituents_people',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'Constituents_people-model.ttl',
        'input_file': 'Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Constituents_people'
    },
    {
        'path': repo_path,
        'name': 'Constituents_role',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Constituents_role-model.ttl',
        'input_file': 'Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Constituents_role'
    },
    # {
    #     'path': repo_path,
    #     'name': 'Dimensions',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'Dimensions.csv-model.ttl',
    #     'input_file': 'Dimensions.csv',
    #     'input_file_type': 'csv',
    #     'output_file_name': 'Dimensions'
    # },
    {
        'path': repo_path,
        'name': 'Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Geography-model.ttl',
        'input_file': 'Geography.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Geography'
    },
    {
        'path': repo_path,
        'name': 'Media_primary',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Media_primary-model.ttl',
        'input_file': 'Media_primary.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Media_primary'
    },
    {
        'path': repo_path,
        'name': 'Medium',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Medium-model.ttl',
        'input_file': 'Medium.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Medium'
    },
    # {
    #     'path': repo_path,
    #     'name': 'Objects',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'Objects-model.ttl',
    #     'input_file': 'Objects.csv',
    #     'input_file_type': 'csv',
    #     'output_file_name': 'Objects'
    # },
    {
        'path': repo_path,
        'name': 'Other_titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Other_titles-model.ttl',
        'input_file': 'Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Other_titles'
    },
    {
        'path': repo_path,
        'name': 'Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'Titles-model.ttl',
        'input_file': 'Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'Titles'
    },
]