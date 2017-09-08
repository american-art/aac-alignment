#!/usr/bin/env python
import codecs
import shutil
import json
from auto_import import *

TMP_FOLDER = './tmp'
TMP_ZIP_OUTPUT = os.path.join(TMP_FOLDER, 'output')
TMP_ZIP_FILE_PATH = os.path.join(TMP_FOLDER, 'temp.n3.zip')

def download_file(url):
    r = requests.get(url, stream=True)
    with open(TMP_ZIP_FILE_PATH, 'wb') as f:
        for chunk in r.iter_content(chunk_size=10240): # 10MB
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == '__main__':
    # python auto_import_from_url.py [config file format in json]
    # python auto_import_from_url.py data_file_config.json

    if not os.path.exists(TMP_FOLDER):
        os.mkdir(TMP_FOLDER)
    if os.path.exists(TMP_ZIP_OUTPUT):
        shutil.rmtree(TMP_ZIP_OUTPUT)


    # read config
    config_file_path = sys.argv[1]
    with codecs.open(config_file_path, 'r') as f:
        config_list = json.loads(f.read())
    # print config_list

    # download data
    for c in config_list:
        c['dataset'] = TDB_DATASET_NAME if c['dataset'] == 'pro' else TDB_DEV_DATASET_NAME
        if c['drop_graph']:
            drop_graph(c['dataset'], c['museum'])

        for url in c['data']:
            download_file(url)
            zip_extract(TMP_ZIP_FILE_PATH, TMP_ZIP_OUTPUT)

            for o_name in os.listdir(TMP_ZIP_OUTPUT):
                file = os.path.join(TMP_ZIP_OUTPUT, o_name)
                if os.path.isfile(file) and o_name.endswith('.n3'):

                    chunk_size = 100000 # read 100k lines everytime
                    with codecs.open(file, 'r') as f:
                        while True:
                            next_chunk = ''.join(list(islice(f, chunk_size)))
                            if not next_chunk:
                                break

                            import_data(next_chunk, c['dataset'], GRAPH_BASE_URL + c['museum'])

            os.remove(TMP_ZIP_FILE_PATH)
            shutil.rmtree(TMP_ZIP_OUTPUT)
