import json
import requests
import os

# Load the JSON file
with open('objects.json', 'r') as f:
    data = json.load(f)

# Change the current directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define the models directory
models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'models')

# Loop over the objects in the dictionary
for obj_name, obj_data in data.items():
    url = obj_data['model_urls']
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content of the response to a file in the models directory
        with open(os.path.join(models_dir, f'{obj_name}.glb'), 'wb') as f:
            f.write(response.content)