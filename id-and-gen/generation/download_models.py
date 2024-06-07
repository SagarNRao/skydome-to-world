import json
import requests
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('objects.json', 'r') as f:
    data = json.load(f)

models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','Blender','models')

for obj_name, obj_data in data.items():
    url = obj_data['model_urls']
    response = requests.get(url)

    if response.status_code == 200:
        with open(os.path.join(models_dir, f'{obj_name}.glb'), 'wb') as f:
            f.write(response.content)