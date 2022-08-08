import bpy
import os
from random import randint

# This script imports all fbx files from the highest level folder and places copies of each fbx in random locations in the scene.
# The new scene is exported as an fbx to the 'full-rooms' folder.
#====

# Blend file location
basedir = os.path.dirname(bpy.data.filepath)

# Import all fbx from folder into Blend project
# get list of all files in directory
file_list = sorted(os.listdir(basedir))
# get a list of files ending in 'fbx'
obj_list = [item for item in file_list if item.endswith('.fbx')]


bpy.ops.object.select_all(action='DESELECT')

# Move the selected fbx to a new random location. Used for placing new and duplicated fbx imports.
def place_fbx_at_rand_transform():
    x = randint(-10,10)
    y = randint(-10,10)
    z = randint(-3,3)
    obj = bpy.context.selected_objects[0] # returns a list
    print(obj)
    #obj = selection_objects[0] # since selection_object returns a list of 1 element, we want first element, which is of type 'bpy_types.Object'
    obj.location = (x,y,z)   
    

# loop through the strings in obj_list and add the fbx files to the scene. 
# For each fbx file, duplicate and place randomly 4 times. 
# When fbx gets imported, it will show up in scene with its native location and rotation (aka 0,0,0).

# ---
count = 4
print (obj_list)
for item in obj_list:
    # Place the original fbx in scene with native transform. 
    path_to_file = os.path.join(basedir, item)
    bpy.ops.import_scene.fbx(filepath = path_to_file)
    
    # Move the original fbx to a new location.
    place_fbx_at_rand_transform()
    
    # Place copies of the original fbx at random locations. 
    for c in range(0,count):
        #place_fbx_at_rand_transform()  
        bpy.ops.object.duplicate()
        place_fbx_at_rand_transform()
        # bpy.ops.object.select_all(action='DESELECT') # Not needed as deselected after finishing each iteration of loop automatically        

# ---


# Export as fbx
if not basedir:
    raise Exception("Blend file is not saved")
    
#name = bpy.path.clean_name(cube_obj.name)
#fn = os.path.join(basedir, name)
fn = os.path.join(basedir, "full-rooms\\full_room_1")

bpy.ops.export_scene.fbx(filepath=fn + ".fbx")
