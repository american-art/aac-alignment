#!/usr/bin/env python


import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'saam'
repo_path = '../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/saam/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    {
        'path': repo_path,
        'name': 'Artist',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebArtistBioImages-model.ttl',
        'input_file': 'WebArtistBioImages.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebArtistBioImages',
    },
    {
        'path': repo_path,
        'name': 'Artist',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebArtistBio-model.ttl',
        'input_file': 'WebArtistBio.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebArtistBio',
    },
    {
        'path': repo_path,
        'name': 'Artist',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebConAltNames-model.ttl',
        'input_file': 'WebConAltNames.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebConAltNames',
    },
    {
        'path': repo_path,
        'name': 'Artist',
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
        'name': 'Artist',
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
        'name': 'Artist',
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
        'name': 'Artist',
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
        'name': 'Artist',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebMakers_view-model.ttl',
        'input_file': 'WebMakers_view.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebMakers_view',
    },
    {
        'path': repo_path,
        'name': 'Objects',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
        'context_uri': context_uri,
        'model_file': 'WebObjCaption-model.ttl',
        'input_file': 'WebObjCaption.csv',
        'input_file_type': 'csv',
        'output_file_name': 'WebObjCaption',
    },
]