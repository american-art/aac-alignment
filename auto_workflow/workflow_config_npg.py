#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'npg'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/npg/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
         'path': repo_path,
         'name': 'NPGConAltNames',
         'base_uri': base_uri,
         'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
         'context_uri': context_uri,
         'model_file': 'NPGConAltNames2-model.ttl',
         'input_file': 'NPGConAltNames3.csv',
         'input_file_type': 'csv',
         'output_file_name': 'NPGConAltNames2'
    },
    {
        'path': repo_path,
        'name': 'NPGConstituents',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'NPGConstituents2-model.ttl',
        'input_file': 'NPGConstituents3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGConstituents2'
    },
    {
        'path': repo_path,
        'name': 'NPGConThesTerms',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'NPGConThesTerms2-model.ttl',
        'input_file': 'NPGConThesTerms3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGConThesTerms2'
    },
    {
        'path': repo_path,
        'name': 'NPGDimsParsed',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGDims-model.ttl',
        'input_file': 'NPGObjDimsParsed3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGDims'
    },
    {
        'path': repo_path,
        'name': 'NPGObjConXrefs',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjConXrefs2-model.ttl',
        'input_file': 'NPGObjConXrefs3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjConXrefs2'
    },
    {
        'path': repo_path,
        'name': 'NPGObjects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjects2-model.ttl',
        'input_file': 'NPGObjects3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjects2'
    },
    {
        'path': repo_path,
        'name': 'NPGObjProvenance',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjProvenance_2-model.ttl',
        'input_file': 'NPGObjProvenance3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjProvenance_2'
    },
    {
        'path': repo_path,
        'name': 'NPGObjTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjTitles2-model.ttl',
        'input_file': 'NPGObjTitles3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjTitles2',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'NPGObjAltTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjAltTitles2-model.ttl',
        'input_file': 'NPGObjTitles2.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjAltTitles2',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'NPGObjURLs',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjURLs-model.ttl',
        'input_file': 'NPGWebObjectURLs.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjURLs'
    },
    {
        'path': repo_path,
        'name': 'NPGWebImageURLs',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGWebImageURLs_2-model.ttl',
        'input_file': 'NPGWebImageURLs.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGWebImageURLs_2'
    },
    {
        'path': repo_path,
        'name': 'NPGObjThesTerms',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjThesTerms-model.ttl',
        'input_file': 'NPGObjThesTerms3.csv',
        'input_file_type': 'csv',
        'output_file_name': 'NPGObjThesTerms'
    }
]
