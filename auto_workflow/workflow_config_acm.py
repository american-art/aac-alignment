#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'acm'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.cartermuseum.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist1.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist1'
    },
    {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist2.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist2'
    },
    {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist3.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist3'
   },
   {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist4.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist4'
   },
   {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist5.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist5'
   },
   {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist6.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist6'
   },
   {
       'path': repo_path,
       'name': 'acm-artist',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'acm-artist-model.ttl',
       'input_file': 'acm-artist7.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-artist7'
   },
   {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects1.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects1'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects2.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects2'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects3.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects3'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects4.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects4'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects5.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects5'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects6.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects6'
    },
    {
       'path': repo_path,
       'name': 'acm-objects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-objects-model.ttl',
       'input_file': 'acm-objects7.xml',
       'input_file_type': 'xml',
       'output_file_name': 'acm-objects7'
    },
    {
       'path': repo_path,
       'name': 'acm-media',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'acm-media-model.ttl',
       'input_file': 'ACMAA_Media_data_final.csv',
       'input_file_type': 'csv',
       'output_file_name': 'acm-media'
    },
    {
       'path': repo_path,
       'name': 'ACM_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription/DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'ACM_Metadata-model.ttl',
       'input_file': 'ACM_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'ACM_Metadata'
    }
]
  
