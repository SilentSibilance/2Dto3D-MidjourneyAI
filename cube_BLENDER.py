import bpy
from random import randint
bpy.ops.mesh.primitive_cube_add()

# Spawn multiple randomly spaced cubes
#how many cubes you want to add
#count = 10

#for c in range(0,count):
#    x = randint(-10,10)
#    y = randint(-10,10)
#    z = randint(-10,10)
#    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

bpy.ops.material.new()