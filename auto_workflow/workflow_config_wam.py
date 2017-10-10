#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'wam'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.thewalters.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents_individual',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Constituents_individual-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Constituents_individual',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents_institution',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Constituents_institution-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Constituents_institution',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents_individual_death',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Constituents_individual_death-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Constituents_individual_death',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents_individual_birth',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Constituents_individual_birth-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Constituents_individual_birth',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Constituents_role',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Constituents_role-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Constituents_role'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Culture',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Culture-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Constituents_V3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Culture',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Dimensions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Dimensions-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Dimensions_v2.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Dimensions'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Geography-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Geography.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Geography',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Media',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Media-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Media_v3.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Media'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Objects-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Objects_v3_9-26-17.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Objects'
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Titles-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Titles_v2_11-2016.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Titles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WAM_AAC_Other_titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_AAC_Other_titles-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Titles_v2_11-2016.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_AAC_Other_titles',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    }
]
