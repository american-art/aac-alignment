#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'saam'
repo_path = '../../aac-repos/' + repo_name
base_uri = 'http://data.americanart.si.edu/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'WebArtistBio',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebArtistBio-model.ttl',
        'input_file': 'WebArtistBio.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebArtistBio'
    },
    #{
     #   'path': repo_path,
     #   'name': 'WebArtistBioImages',
     #   'base_uri': base_uri,
     #   'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
     #   'context_uri': context_uri,
     #   'model_file': 'WebArtistBioImages-model.ttl',
     #   'input_file': 'WebArtistBioImages.csv',
     #   'input_file_type': 'csv',
     #   'output_file_name': 'WebArtistBioImages'
    #},
    {
        'path': repo_path,
        'name': 'WebConAltNames',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConAltNames-model.ttl',
        'input_file': 'WebConAltNames.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConAltNames'
    },
    {
        'path': repo_path,
        'name': 'WebConDatesBirth',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConDatesBirth-model.ttl',
        'input_file': 'WebConDates.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConDatesBirth',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WebConDatesDeath',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConDatesDeath-model.ttl',
        'input_file': 'WebConDates.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConDatesDeath',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WebConGeographyBirth',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConGeographyBirth-model.ttl',
        'input_file': 'WebConGeography.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConGeographyBirth',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WebConGeographyDeath',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConGeographyDeath-model.ttl',
        'input_file': 'WebConGeography.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConGeographyDeath',
        'additional_settings':{'rdf.generation.selection':'DEFAULT_TEST'}
    },
    {
        'path': repo_path,
        'name': 'WebConstituents_institution_view',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConstituents_institution_view-model.ttl',
        'input_file': 'WebConstituents_institution_view.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConstituents_institution_view'
    },
    {
        'path': repo_path,
        'name': 'WebConstituents_person_view',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConstituents_person_view-model.ttl',
        'input_file': 'WebConstituents_person_view.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConstituents_person_view'
    },
    {
        'path': repo_path,
        'name': 'WebMakers_view',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WebMakers_view-model.ttl',
        'input_file': 'WebMakers_view.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebMakers_view'
    },
    {
        'path': repo_path,
        'name': 'WebObjCaption',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WebObjCaption-model.ttl',
        'input_file': 'WebObjCaption.json',
        'input_file_type': 'jsonlines',
        'output_file_name': 'WebObjCaption',
        'num_partitions': 50
    },
    {
        'path': repo_path,
        'name': 'WebObjDescription',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WebObjDescription-model.ttl',
        'input_file': 'WebObjDescription.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebObjDescription',
        'num_partitions': 50
    },
    {
        'path': repo_path,
        'name': 'WebObjectImages',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WebObjectImages.csv-model.ttl',
        'input_file': 'WebObjectImages.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebObjectImages'
    },
    {
        'path': repo_path,
        'name': 'WebObjDimensionsSplit_view',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'WebObjDimensionsSplit_view-model.ttl',
        'input_file': 'WebObjDimensionsSplit_view.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebObjDimensionsSplit_view'
    },
    {
       'path': repo_path,
       'name': 'SAAM_AAC_VoIDDescription',
       'base_uri': base_uri,
       'rdf_root_uri': 'http://rdfs.org/ns/void#DatasetDescription1',
       'context_uri': context_uri,
       'model_file': 'SAAM_Metadata-model.ttl',
       'input_file': 'SAAM_Metadata.json',
       'input_file_type': 'json',
       'output_file_name': 'SAAM_Metadata'
    }
]
