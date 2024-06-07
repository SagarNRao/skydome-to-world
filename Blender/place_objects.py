import bpy
import os
import json
from mathutils import Vector

os.chdir(os.path.join('..','..','..','..','..','..','..','..','Projects','Python','skydome to world','id-and-gen', 'generation'))

objects = []
with open("objects.json",'r') as f:
    data = json.load(f)
    
objects = list(data.keys())

# placing the objects
def place(obj):
    x = data[obj.name]["x"]
    y = data[obj.name]["y"]
    z = data[obj.name]["z"]
    xrot = data[obj.name]["xrot"]
    yrot = data[obj.name]["yrot"]
    zrot = data[obj.name]["zrot"]
    
    obj.location = Vector((x, y, z))
    obj.rotation_euler = Vector((xrot, yrot, zrot))

dir_path = "C:\Projects\Python\skydome to world\Blender\models"
files = os.listdir(dir_path)

for file in files:
    if file.endswith('.glb'):
        file_path = os.path.join(dir_path, file)
        bpy.ops.import_scene.gltf(filepath=file_path)
        
# importing the files
i = 0   
length = len(bpy.data.objects) 
for j in range (1, length):
    if (i == 0):
            i = i + 1
            obj = bpy.data.objects["Mesh1"]
            buffname2 = str(files[1])
            obj.name = buffname2[:-4]
            place(obj)
            print("first")
    elif (i >= 1):
        if 0 < i < 10:
            buffname = "Mesh1." + "00" + str(i)
            print(buffname)
            obj = bpy.data.objects[buffname]
            buffname2 = str(files[i+1])
            obj.name = buffname2[:-4]
            print(obj.name)
            place(obj)
            i = i + 1
        elif 10 < i < 100:
            buffname = "Mesh1." + "0" + str(i)
            print(buffname)
            obj = bpy.data.objects[buffname]
            buffname2 = str(files[i+1])
            obj.name = buffname2[:-4]
            print(obj.name)
            place(obj)
            i = i + 1
        else:
            buffname = "Mesh1." + str(i)
            print(buffname)
            obj = bpy.data.objects[buffname]
            buffname2 = str(files[i+1])
            obj.name = buffname2[:-4]
            print(obj.name)
            place(obj)
            i = i + 1
            
            
