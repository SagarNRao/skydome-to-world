import json
import requests
import os

# os.chdir(r"Blender\id and gen\generation")

with open('objects.json', 'r') as f:
    data = json.load(f)

# Assume that data is a list of URLs
for i, url in enumerate(data):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content of the response to a file
        with open(f'file_{i}', 'wb') as f:
            f.write(response.content)