# Take a UV map png as input. Detect the corners of the UV map segment areas.
# Since working with cube currently, want to find dimensions of one cube surface.
# Also want to find locations of each of 6 cube surfaces.
# Finally, take face_texture images and apply them to each of the 6 respective cube surfaces on the UV map. (This creates a texture file for the cube.)

# Reference documentation: https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html

import cv2 as cv
import numpy as np

input_uv = 'Cube_UV.png'
uv = cv.imread(input_uv)
uv_harris = cv.imread(input_uv)

gray = cv.cvtColor(uv_harris, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
#dst = cv.dilate(dst, None)

uv_harris[dst>0.01*dst.max()] = [0,0,255] #makes corner points red

cv.imshow('Original UV', uv)
cv.imshow('Harris', uv_harris)
cv.imshow('Harris Corners', dst)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
