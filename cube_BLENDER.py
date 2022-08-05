import bpy
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

# Add Material
bpy.ops.material.new()
cube_mat_obj = bpy.data.materials.new(cube_obj.name + '-Material')
cube_mat_obj.use_nodes = True

bsdf = cube_mat_obj.node_tree.nodes["Principled BSDF"]
texImage = cube_mat_obj.node_tree.nodes.new('ShaderNodeTexImage')
bpy.ops.image.open('shark_UV_w_textures.png')
#texImage.image = bpy.data.images.load('shark_UV_w_textures.png')
#cube_mat_obj.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
#box_obj.data.materials.append(cube_mat_obj)


#TODO: attach the created png to the material

#TODO: export as fbx
#bpy.ops.export_scene.fbx()