import bpy
import os
from random import randint

# Add Cube
bpy.ops.mesh.primitive_cube_add()
cube_obj = bpy.context.selected_objects[0]
cube_obj.name = 'MyCube'

# Spawn multiple randomly spaced cubes
#how many cubes you want to add
#count = 10

#for c in range(0,count):
#    x = randint(-10,10)
#    y = randint(-10,10)
#    z = randint(-10,10)
#    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

# Attach the created png to the material
# Add Material
#bpy.ops.material.new()
cube_mat_obj = bpy.data.materials.new(cube_obj.name + '-Material')
cube_mat_obj.use_nodes = True

bsdf = cube_mat_obj.node_tree.nodes["Principled BSDF"]
texImage = cube_mat_obj.node_tree.nodes.new('ShaderNodeTexImage')
#bpy.ops.image.open('shark_UV_w_textures.png')
texImage.image = bpy.data.images.load(filepath = '//shark_UV_w_textures.png')#(allow_path_tokens=True, filepath='', directory='', files=None, hide_props_region=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', use_sequence_detection=True, use_udim_detecting=True)
cube_mat_obj.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
cube_obj.data.materials.append(cube_mat_obj)


# Export as fbx
# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")
    
name = bpy.path.clean_name(cube_obj.name)
fn = os.path.join(basedir, name)

bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
