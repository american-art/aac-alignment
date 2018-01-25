#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'autry'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.theautry.org/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
   {
       'path': repo_path,
       'name': 'AutryCultureMade',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryCultureMade-model.ttl',
       'input_file': 'AutryCultureMade.csv',
       'output_file_name': 'AutryCultureMade'
   },
   {
       'path': repo_path,
       'name': 'AutryDated',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryDated-model.ttl',
       'input_file': 'AutryDated.csv',
       'output_file_name': 'AutryDated'
   },
   {
       'path': repo_path,
       'name': 'AutryMakers',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryMakers-model.ttl',
       'input_file': 'AutryMakers.csv',
       'output_file_name': 'AutryMakers'
   },
   {
       'path': repo_path,
       'name': 'AutryMedia',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryMedia-model.ttl',
       'input_file': 'AutryMedia.csv',
       'output_file_name': 'AutryMedia'
   },
   {
       'path': repo_path,
       'name': 'AutryObjects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryObjects-model.ttl',
       'input_file': 'AutryObjects.csv',
       'output_file_name': 'AutryObjects'
   },
   {
       'path': repo_path,
       'name': 'AutryPubDesc',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'AutryPubDesc-model.ttl',
       'input_file': 'AutryPubDesc.csv',
       'output_file_name': 'AutryPubDesc'
   },
   {
       'path': repo_path,
       'name': 'Autry_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'Autry_Metadata-model.ttl',
       'input_file': 'Autry_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'Autry_Metadata'
    }
]
