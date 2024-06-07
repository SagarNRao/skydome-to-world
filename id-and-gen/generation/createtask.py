import requests
import os
import json
import asyncio
import aiohttp

os.chdir(os.path.dirname(os.path.abspath(__file__)))

objects = []
with open("objects.json",'r') as f:
    data = json.load(f)
    
objects = list(data.keys())

YOUR_API_KEY="msy_rcp6SIBA2Saqkket6IQBDLklfyfT27EgHxiH"

async def send_request(session, thing):
    payload = {
        "mode": "preview",
        "prompt": f"{thing}",
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
        tasks = [send_request(session, thing) for thing in objects]
        responses = await asyncio.gather(*tasks)
    return responses

try:
    response = asyncio.run(main())
except Exception as e:
    print(f"An error occurred: {e}")
    response = []
    
# print("Responses:")
# print(response)

tasks = {obj: res["result"] for obj, res in zip(objects, response)}
    
print("Tasks:")
print(tasks)

for obj in data:
    data[obj]["task_id"] = tasks[obj]
    
with open("objects.json",'w') as f:
    json.dump(data, f, indent=4)