#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'aaa'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/aaa/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
       'path': repo_path,
       'name': 'Item',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'Item-model.ttl',
       'input_file': 'Item.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item'
    },
    {
       'path': repo_path,
       'name': 'Item_Collections',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E78_Collection1',
       'context_uri': context_uri,
       'model_file': 'Item_Collections-model.ttl',
       'input_file': 'Item_Collections.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_Collections'
    },
    {
       'path': repo_path,
       'name': 'Item_DigitalResources',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Thing1',
       'context_uri': context_uri,
       'model_file': 'Item_DigitalResources-model.ttl',
       'input_file': 'Item_DigitalResources.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_DigitalResources'
    },
    {
       'path': repo_path,
       'name': 'Item_Events',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E5_Event1',
       'context_uri': context_uri,
       'model_file': 'Item_Events-model.ttl',
       'input_file': 'Item_Events.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_Events'
    },
    {
       'path': repo_path,
       'name': 'Item_Institutions',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_Institutions-model.ttl',
       'input_file': 'Item_Institutions.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_Institutions'
    },
    {
       'path': repo_path,
       'name': 'Item_People',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_People-model.ttl',
       'input_file': 'Item_People.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_People'
    },
    {
       'path': repo_path,
       'name': 'Item_PeopleOccupations',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_PeopleOccupations-model.ttl',
       'input_file': 'Item_PeopleOccupations.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_PeopleOccupations'
    },
    {
       'path': repo_path,
       'name': 'Item_PeoplePlaces',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
       'context_uri': context_uri,
       'model_file': 'Item_PeoplePlaces-model.ttl',
       'input_file': 'Item_PeoplePlaces.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_PeoplePlaces'
    },
    {
       'path': repo_path,
       'name': 'Item_Subjects',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'Item_Subjects-model.ttl',
       'input_file': 'Item_Subjects.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_Subjects'
    },
    {
       'path': repo_path,
       'name': 'Item_to_Collection',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
       'context_uri': context_uri,
       'model_file': 'Item_to_Collection-model.ttl',
       'input_file': 'Item_to_Collection.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_to_Collection'
    },
    {
       'path': repo_path,
       'name': 'Item_to_type',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E55_Type1',
       'context_uri': context_uri,
       'model_file': 'Item_to_type-model.ttl',
       'input_file': 'Item_to_type.csv',
       'input_file_type': 'csv',
       'output_file_name': 'Item_to_type'
    },
    {
       'path': repo_path,
       'name': 'AAA_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription/DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'AAA_Metadata-model.ttl',
       'input_file': 'AAA_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'AAA_Metadata'
    }
]
  
