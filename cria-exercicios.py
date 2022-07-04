import glob
import os
import os.path as osp
from tkinter import OFF
import slugify
import yaml
import requests

OFFERING = 4
HOSTNAME = f'https://devlife.insper-comp.com.br/api/offerings/{OFFERING}/exercises/'
AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '')

if __name__ == '__main__':
    for meta in glob.glob('**/meta.yml', recursive=True):
        folder = osp.dirname(meta)
        slug = slugify.slugify(folder)

        with open(meta, encoding='utf-8') as f:
            metadata = yaml.safe_load(f)
            if metadata is None:
                metadata = {}
            metadata['slug'] = slug
            metadata['offering'] = OFFERING
            metadata['type'] = 'CODE'
            metadata['group'] = 'extra'
            metadata['url'] = folder
            if not 'title' in metadata:
                metadata['title'] = osp.split(folder)[1].replace('_', ' ').capitalize()
            if not 'topic' in metadata:
                metadata['topic'] = osp.split(folder)[0]

        with open(meta, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f)
    
        print('Encontrado exercicio', folder)
        if AUTH_TOKEN:

            headers = {
                'Authorization': f'Token {AUTH_TOKEN}',
            }
            ret = requests.post(HOSTNAME, data=metadata, headers=headers)
            print(ret)
            assert ret.status_code == 201


        
        

