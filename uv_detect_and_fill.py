# Take a UV map png as input. Detect the corners of the UV map segment areas.
# Since working with cube currently, want to find dimensions of one cube surface.
# Also want to find locations of each of 6 cube surfaces.
# Finally, take face_texture images and apply them to each of the 6 respective cube surfaces on the UV map. (This creates a texture file for the cube.)

# Reference documentation: https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

input_uv = 'Cube_UV.png'
uv_original = cv.imread(input_uv)
uv_harris = cv.imread(input_uv)
uv_pyshitomasi = cv.imread(input_uv)

# Create gayscale version of image.
gray = cv.cvtColor(uv_original, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris
dst = cv.cornerHarris(gray, 2, 3, 0.04)
#dst = cv.dilate(dst, None)
uv_harris[dst>0.01*dst.max()] = [0,0,255] #makes corner points red

# Py Shi Tomasi
corners = cv.goodFeaturesToTrack(gray, 18, 0.01, 10) # 18 is number of corners to track
corners = np.int0(corners) # don't forget this line. Research this line further.

for i in corners:
    x,y = i.ravel()
    cv.circle(uv_pyshitomasi,(x,y),3,255,-1)

cv.imshow('Original UV', uv_original)
# Harris
#cv.imshow('Harris', uv_harris)
#cv.imshow('Harris Corners', dst)
# Py Shi Tomasi
# cv.imshow('Py Shi Tomasi', corners) # Note: this doesn't work - can't show as image directly as output as array. Need to plot array.
cv.imshow('Py Shi Tomasi UV', uv_pyshitomasi)
plt.imshow(uv_pyshitomasi)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
