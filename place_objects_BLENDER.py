import bpy
import os
from random import randint


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
    selection_objects = bpy.context.selected_objects # returns a list
    obj = selection_objects[0] # since selection_object returns a list of 1 element, we want first element, which is of type 'bpy_types.Object'
    obj.location = (x,y,z)   
    

# loop through the strings in obj_list and add the fbx files to the scene. 
# For each fbx file, duplicate and place randomly 4 times. 
# When fbx gets imported, it will show up in scene with its native location and rotation (aka 0,0,0).

# ---
count = 4
for item in obj_list:
    # Place the original fbx in scene with native transform. 
    path_to_file = os.path.join(basedir, item)
    bpy.ops.import_scene.fbx(filepath = path_to_file)
    
    # Move the original fbx to a new location.
    place_fbx_at_rand_transform()  
    
    # Place copies of the original fbx at random locations. 
    for c in range(0,count):
        bpy.ops.object.duplicate()
        place_fbx_at_rand_transform()  
      # bpy.ops.object.select_all(action='DESELECT') # Not needed as deselected after finishing each iteration of loop automatically        

# ---




# Add Cube
#bpy.ops.mesh.primitive_cube_add()
#cube_obj = bpy.context.selected_objects[0]
#cube_obj.name = 'MyCube'

# Spawn multiple randomly spaced cubes
#how many cubes you want to add
#count = 10

#for c in range(0,count):
#    x = randint(-10,10)
#    y = randint(-10,10)
#    z = randint(-10,10)
#    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

# Scale the cube - OPTIONAL
#cube_obj.scale = (1,1,2)

# Attach the created png to the material
# Add Material
#bpy.ops.material.new()
#cube_mat_obj = bpy.data.materials.new(cube_obj.name + '-Material')
#cube_mat_obj.use_nodes = True

#bsdf = cube_mat_obj.node_tree.nodes["Principled BSDF"]
#texImage = cube_mat_obj.node_tree.nodes.new('ShaderNodeTexImage')
#bpy.ops.image.open('shark_UV_w_textures.png')
#texImage.image = bpy.data.images.load(filepath = '//red_room_3_UV_w_textures.png')#(allow_path_tokens=True, filepath='', directory='', files=None, hide_props_region=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', use_sequence_detection=True, use_udim_detecting=True)
#cube_mat_obj.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
#cube_obj.data.materials.append(cube_mat_obj)


# Export as fbx
#if not basedir:
#    raise Exception("Blend file is not saved")
    
#name = bpy.path.clean_name(cube_obj.name)
#fn = os.path.join(basedir, name)
#fn = os.path.join(basedir, "red_room_3")

#bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
