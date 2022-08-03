# Take a UV map png as input. Detect the corners of the UV map segment areas.
# Since working with cube currently, want to find dimensions of one cube surface.
# Also want to find locations of each of 6 cube surfaces.
# Finally, take face_texture images and apply them to each of the 6 respective cube surfaces on the UV map. (This creates a texture file for the cube.)

# Reference documentation: https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

input_uv = 'Cube_UV_condensed.png'
uv_original = cv.imread(input_uv)
uv_harris = cv.imread(input_uv)
uv_pyshitomasi = cv.imread(input_uv)
uv_corner_checker = cv.imread(input_uv)

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

# TODO: Lazy algorithm to get distance between two corner points. Assume all UV faces have same dimensions.
# Distance between two points = dimension for UV face.
# use Euclidean distance. (This works because perfect square. May not work for more complex shapes?)
# FIRST! Identify which two points are closest. Sort the array of corners in asscending x order.
# I am lazy and notice that I don't need to do the above yet, as points are sorted into neat pairs.
# Lazy should definitely be my search key word for fixing sloppy code.
column_index = 1
corners_list = corners.tolist() #list of lists. NOTE this goes 3 layers deep, with extraneous layer around coordinate pair.
corners_sorted = sorted(corners_list)

# Clean up corner points data. Artifacts left in from corner detection algorithm will not always correctly place two corners with the same x (or y) value correctly and may be off by one.
#Noted issue: With Py Shi Tomasi detection, do not get the same exact row or column when it should line up.
# ex.  256 & 257
# Iterate through sorted corners list. When two points are off by 1 ONLY, set higher value to lower. ex 257 -> 256. Perform for both x and y.
# Comparing corners_sorted[0] to corners_sorted[1], etc.
# Decreasing corners_sorted[1] by 1 if needed.
for count, i in enumerate(corners_sorted[:-1], start=1): # i is higher value. List sliced to be one less than length.
    print("pair")
    print(i[0][0])
    print(corners_sorted[count][0][0])
    if i[0][0] + 1 == corners_sorted[count][0][0]:
        corners_sorted[count][0][0] = corners_sorted[count][0][0] - 1

print("list type: ")
print(corners_list[2][0][1])


dist = np.linalg.norm(corners[0] - corners[1]) # distance between first and second point
#TODO: distance between points must return integer. This all could likely be a function.
# EXERCISE FOR FUN: Find distance between all points. Sort distances in asscending order.


# DISPLAY!
cv.imshow('Original UV', uv_original)
# Harris
#cv.imshow('Harris', uv_harris)
#cv.imshow('Harris Corners', dst)
# Py Shi Tomasi
# cv.imshow('Py Shi Tomasi', corners) # Note: this doesn't work - can't show as image directly as output as array. Need to plot array.
cv.imshow('Py Shi Tomasi UV', uv_pyshitomasi)
plt.imshow(uv_pyshitomasi)

print(corners)
#print("Corners unsorted list: ", corners_list)
#print("Corners sorted array:", corners_sorted)
#print("Corners type: ", type(corners))
#print("Distance between points: ", dist)

print("dst:   ", dst.max())

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

# TODO: Handle cases where corner dectection is off by 2 pixels.
# TODO: Handle y coordinate sorting and corner artifact smoothing.
