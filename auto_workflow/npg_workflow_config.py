#!/usr/bin/env python

import logging

LOG_LEVEL = logging.INFO
ZIP_OUTPUT = True

repo_name = 'npg'
repo_path = './../../aac-repos/' + repo_name
base_uri = 'http://data.americanartcollaborative.org/npg/'
context_uri = 'https://github.com/american-art/aac-alignment/blob/master/karma-context.json'
REPO_CONFIG = [
    # {
    #     'path': repo_path,
    #     'name': 'NPGBibReferences',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E31_Document1',
    #     'context_uri': context_uri,
    #     'model_file': 'npgbibreferences-model.ttl',
    #     'input_file': 'npgbibreferences.csv',
    #     'output_file_name': 'npgbibreferences'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGConAltNames',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGConAltNames2-Institutions-model.ttl',
    #     'input_file': 'NPGConAltNames2.csv',
    #     'output_file_name': 'NPGConAltNames2-Institutions'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGConAltNames',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGConAltNames2-People-model.ttl', # different model
    #     'input_file': 'NPGConAltNames2.csv',
    #     'output_file_name': 'NPGConAltNames2-People'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGConstituents',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGConstituents2-People-model.ttl',
    #     'input_file': 'NPGConstituents2.csv',
    #     'output_file_name': 'NPGConstituents2-People'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGConThesTerms',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E39_Actor1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGConThesTerms2-model.ttl',
    #     'input_file': 'NPGConThesTerms2.csv',
    #     'output_file_name': 'NPGConThesTerms2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGDimsParsedUpdate2May',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGDimsParsedUpdate2May-model.ttl',
    #     'input_file': 'NPGDimsParsedUpdate2May.csv',
    #     'output_file_name': 'NPGDimsParsedUpdate2May'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGExhibitionObjXrefs',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/PC16_used_specific_object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGExhibitionObjXrefs2-model.ttl',
    #     'input_file': 'NPGExhibitionObjXrefs2.csv',
    #     'output_file_name': 'NPGExhibitionObjXrefs2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGExhibitions',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/PC16_used_specific_object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGExhibitions2-model.ttl',
    #     'input_file': 'NPGExhibitions2.csv',
    #     'output_file_name': 'NPGExhibitions2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjConXrefs',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjConXrefs2-model.ttl',
    #     'input_file': 'NPGObjConXrefs2.csv',
    #     'output_file_name': 'NPGObjConXrefs2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjects',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjects2-model.ttl',
    #     'input_file': 'NPGObjects2.csv',
    #     'output_file_name': 'NPGObjects2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjExhText',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjExhText2-model.ttl',
    #     'input_file': 'NPGObjExhText2.csv',
    #     'output_file_name': 'NPGObjExhText2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjProvenance',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjProvenance_2-model.ttl',
    #     'input_file': 'NPGObjProvenance_2.csv',
    #     'output_file_name': 'NPGObjProvenance_2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjThesTerms',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjThesTerms2-model.ttl',
    #     'input_file': 'NPGObjThesTerms2.csv',
    #     'output_file_name': 'NPGObjThesTerms2'
    # },
    {
        'path': repo_path,
        'name': 'NPGObjTitles',
        'base_uri': base_uri,
        'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
        'context_uri': context_uri,
        'model_file': 'NPGObjTitles2-model.ttl',
        'input_file': 'NPGObjTitles2.csv',
        'output_file_name': 'NPGObjTitles2'
    },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjURLs',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjURLs-model.ttl',
    #     'input_file': 'NPGObjURLs.csv',
    #     'output_file_name': 'NPGObjURLs'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGObjWebLabels',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGObjWebLabels2-model.ttl',
    #     'input_file': 'NPGObjWebLabels2.csv',
    #     'output_file_name': 'NPGObjWebLabels2'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGRefObjXrefs',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E31_Document1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGRefObjXrefs-model.ttl',
    #     'input_file': 'NPGRefObjXrefs.csv',
    #     'output_file_name': 'NPGRefObjXrefs'
    # },
    # {
    #     'path': repo_path,
    #     'name': 'NPGWebImageURLs',
    #     'base_uri': base_uri,
    #     'rdf_root_uri': 'http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object1',
    #     'context_uri': context_uri,
    #     'model_file': 'NPGWebImageURLs_2-model.ttl',
    #     'input_file': 'NPGWebImageURLs_2.csv',
    #     'output_file_name': 'NPGWebImageURLs_2'
    # },
]