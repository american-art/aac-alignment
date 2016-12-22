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
        'name': 'WAM_XMLExport_AAC_Exhibitions',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_XMLExport_AAC_Exhibitions-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Exhibitions.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_XMLExport_AAC_Exhibitions'
    },
    {
        'path': repo_path,
        'name': 'WAM_XMLExport_AAC_Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_XMLExport_AAC_Geography-Place_Depicted-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Geography.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_XMLExport_AAC_Geography-Place_Depicted'
    },
    {
        'path': repo_path,
        'name': 'WAM_XMLExport_AAC_Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E11_Modification1',
        'context_uri': context_uri,
        'model_file': 'WAM_XMLExport_AAC_Geography-Place_of_Binding-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Geography.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_XMLExport_AAC_Geography-Place_of_Binding'
    },
    {
        'path': repo_path,
        'name': 'WAM_XMLExport_AAC_Geography',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_XMLExport_AAC_Geography-Place_of_Origin-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Geography.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_XMLExport_AAC_Geography-Place_of_Origin'
    },
    {
        'path': repo_path,
        'name': 'WAM_XMLExport_AAC_Titles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WAM_XMLExport_AAC_Titles-model.ttl',
        'input_file': 'WAM_XMLExport_AAC_Titles.xml',
        'input_file_type': 'xml',
        'output_file_name': 'WAM_XMLExport_AAC_Titles'
    },
]