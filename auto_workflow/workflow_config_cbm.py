#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'cbm'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/cbm/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'CBMAA_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Constituents-model.ttl',
        'input_file': 'LOD CBMAA Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Constituents'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Exhibitions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Exhibitions-model.ttl',
        'input_file': 'LOD CBMAA Exhibitions.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Exhibitions'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Objects-model.ttl',
        'input_file': 'LOD CBMAA Objects_formatted.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Objects'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Titles-model.ttl',
        'input_file': 'LOD CBMAA Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Titles'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_OtherTitles-model.ttl',
        'input_file': 'LOD CBMAA Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_OtherTitles'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_UnknownTitles-model.ttl',
        'input_file': 'LOD CBMAA Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_UnknownTitles'
    },
    {
        'path': repo_path,
        'name': 'PG_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Constituents-model.ttl',
        'input_file': 'LOD PG Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Constituents'
    },
    {
        'path': repo_path,
        'name': 'PG_Exhibitions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Exhibitions-model.ttl',
        'input_file': 'LOD PG Exhibitions.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Exhibitions'
    },
    {
        'path': repo_path,
        'name': 'PG_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Objects-model.ttl',
        'input_file': 'LOD PG Objects_formatted.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Objects'
    },
    {
        'path': repo_path,
        'name': 'PG_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Titles-model.ttl',
        'input_file': 'LOD PG Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Titles'
    },
    {
        'path': repo_path,
        'name': 'PG_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_OtherTitles-model.ttl',
        'input_file': 'LOD PG Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_OtherTitles'
    },
    {
        'path': repo_path,
        'name': 'PG_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_UnknownTitles-model.ttl',
        'input_file': 'LOD PG Titles.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_UnknownTitles'
    }
]
