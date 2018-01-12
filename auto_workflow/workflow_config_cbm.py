#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'cbm'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.crystalbridges.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'CBMAA_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Constituents-model.ttl',
        'input_file': 'LOD CBMAA Constituents.csv',
        'input_file_type': 'csv',
        
        'output_file_name': 'CBMAA_Constituents'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Objects-model.ttl',
        'input_file': 'LOD CBMAA Objects v2 1-2018.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Objects'
    },
    {
        'path': repo_path,
        'name': 'CBMAA_OtherTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_OtherTitles-model.ttl',
        'input_file': 'CBMAA Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_OtherTitles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Titles-model.ttl',
        'input_file': 'CBMAA Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Titles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'CBMAA_UnknownTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_UnknownTitles-model.ttl',
        'input_file': 'CBMAA Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_UnknownTitles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'CBMAA_URLs',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_URLs-model.ttl',
        'input_file': 'CBMAA Images_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_URLs',
    },
    {
        'path': repo_path,
        'name': 'CBMAA_Roles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'CBMAA_Roles-model.ttl',
        'input_file': 'LOD CBMAA Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'CBMAA_Roles',
    },
    {
        'path': repo_path,
        'name': 'PG_Constituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'PG_Constituents-model.ttl',
        'input_file': 'LOD PG Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Constituents'
    },
    {
        'path': repo_path,
        'name': 'PG_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Objects-model.ttl',
        'input_file': 'LOD PG Objects v2 1-2018.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Objects'
    },
    {
        'path': repo_path,
        'name': 'PG_OtherTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_OtherTitles-model.ttl',
        'input_file': 'PG Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_OtherTitles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'PG_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Titles-model.ttl',
        'input_file': 'PG Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Titles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'PG_UnknownTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_UnknownTitles-model.ttl',
        'input_file': 'PG Titles_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_UnknownTitles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'PG_URLs',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_URLs-model.ttl',
        'input_file': 'PG Images_with_header.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_URLs'
    },
    {
        'path': repo_path,
        'name': 'PG_Roles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'PG_Roles-model.ttl',
        'input_file': 'LOD PG Constituents.csv',
        'input_file_type': 'csv',
        'output_file_name': 'PG_Roles'
    },
    {
       'path': repo_path,
       'name': 'CBM_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription/DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'CBM_Metadata-model.ttl',
       'input_file': 'CBM_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'AAA_Metadata'
    }
]
