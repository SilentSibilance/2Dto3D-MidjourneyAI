# Create an stl mesh from given coordinates in an image. Assume the image has rectangular sections that will be protruded forward in the mesh. Assume base mesh is a cube.
# To allow for the rectangle protrustion, additional vertices must be added to the face for proper tri layout.

import numpy as np
from stl import mesh


#Create object with corner of cube at origin, for ease.
#OBJECT IS NOT CENTRED!
#scale coordinates of rectangle on image from pixel of 400x400 to mesh scale of 4x4
#upper left coordinate: (40, 120) -> (0.4, 1.2)
#lower right coordinate: (120, 320) -> (1.2, 3.2)

#upper right coordinate: (120, 120) -> (1.2, 1.2)
#lower left coordinate: (40, 320) -> (0.4, 3.2)

# Thrust is the distance the rectangle sticks out from the face of the base cube.
thrust = 0.6

# Define the 8 vertices of the base cube & 8 vertices of rectangle protrusion
# Plus the additional 8 vertices required for tris on the complex face.
vertices = np.array([\
    [0, 0, 0], #0 - base cube
    [+4, 0, 0], #1 - base cube
    [+4, +4, 0], #2 - base cube
    [0, +4, 0], #3 - base cube
    [0, 0, +4], #4 - base cube
    [+4, 0, +4], #5 - base cube
    [+4, +4, +4], #6 - base cube
    [0, +4, +4], #7 - base cube
    [0, +1.2, +4], #8 - base cube adtl points
    [0, +3.2, +4], #9 - base cube adtl points
    [4, +1.2, +4], #10 - base cube adtl points
    [4, +3.2, +4], #11 - base cube adtl points
    [+1.2, 0, +4], #12 - base cube adtl points
    [+3.2, 0, +4], #13 - base cube adtl points
    [+1.2, 4, +4], #14 - base cube adtl points
    [+3.2, 4, +4], #15 - base cube adtl points
    [0.4, +1.2, +4], #16 - rectangle -0
    [1.2, +1.2, +4], #17 - rectangle -1
    [0.4, +3.2, +4], #18 - rectangle -2
    [1.2, +3.2, +4], #19 - rectangle -3
    [0.4, +1.2, +(4+thrust)], #20 - rectangle -4
    [1.2, +1.2, +(4+thrust)], #21 - rectangle -5
    [0.4, +3.2, +(4+thrust)], #22 - rectangle -6
    [1.2, +3.2, +(4+thrust)] #23 - rectangle -7
    ])


# STL files require all faces to be defined as triangles using the right hand rule to define the normal.
# Coordinates must be defined in a counter-clockwise fashion.

# Define the 12 triangles composing the cube
faces = np.array([\
    # Base cube start
    [0,3,1],
    [1,3,2],
    [0,4,7],
    [0,7,3],
    [4,5,6],
    [4,6,7],
    [5,1,2],
    [5,2,6],
    [2,3,6],
    [3,7,6],
    [0,1,5],
    [0,5,4],
    #Base cube end
    #Complex face base cube start
    #Complex face base cube end
    #Protrusion start
    [18,22,19],
    [19,22,23],
    [16,17,21],
    [21,20,16],
    [18,16,20],
    [20,22,18],
    [19,17,21],
    [21,23,19],
    [21,20,22],
    [22,23,21],
    #Protrusion end])
