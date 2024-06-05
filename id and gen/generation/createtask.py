import requests
import os
import json
import asyncio
import aiohttp

os.chdir(os.path.dirname(os.path.abspath(__file__)))

tasks = {}
objects = []
with open("objects.json",'r') as f:
    data = json.load(f)
    
objects = list(data.keys())

YOUR_API_KEY="msy_rcp6SIBA2Saqkket6IQBDLklfyfT27EgHxiH"

async def send_request(session, thing):
    payload = {
        "mode": "preview",
        "prompt": thing,
        "art_style": "realistic",
        "negative_prompt": "low quality, low resolution, low poly, ugly"
    }
    headers = {
        "Authorization": f"Bearer {YOUR_API_KEY}"
    }
    async with session.post("https://api.meshy.ai/v2/text-to-3d", headers=headers, json=payload) as response:
        response.raise_for_status()
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for thing in objects:
            tasks.append(send_request(session, thing))
        return await asyncio.gather(*tasks)
        
        
# Run the main function
try:
    response = asyncio.run(main())
except:
    response = []

tasks = {obj: res["result"] for obj, res in zip(objects, response)}
    
print("Tasks:")
print(tasks)

for obj in data:
    data[obj]["task_id"] = tasks[obj]
    
with open("objects.json",'w') as f:
    json.dump(data, f, indent=4)