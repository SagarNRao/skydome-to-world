import requests
import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

YOUR_API_KEY = "msy_rcp6SIBA2Saqkket6IQBDLklfyfT27EgHxiH"

with open("objects.json", 'r') as f:
    data = json.load(f)
    for obj in data:
        task_id = data[obj]["task_id"]
        headers = {
            "Authorization": f"Bearer {YOUR_API_KEY}"
        }
        response = requests.get(
            f"https://api.meshy.ai/v2/text-to-3d/{task_id}",
            headers=headers,
        )
        
        response_dict = response.json()
        
        for obj in data:
            data[obj]["model_urls"] = response_dict["model_urls"]["glb"]

with open ("objects.json", 'w') as f:
    json.dump(data, f, indent=4)
