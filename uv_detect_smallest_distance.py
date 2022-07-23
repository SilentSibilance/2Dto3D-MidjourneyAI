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

def find_corners():
    #  -- Harris --
    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    #dst = cv.dilate(dst, None)
    uv_harris[dst>0.01*dst.max()] = [0,0,255] #makes corner points red
    # ----

    # -- Py Shi Tomasi --
    corners = cv.goodFeaturesToTrack(gray, 18, 0.01, 10) # 18 is number of corners to track
    corners = np.int0(corners) # don't forget this line. Research this line further.

    for i in corners:
        x,y = i.ravel()
        cv.circle(uv_pyshitomasi,(x,y),3,255,-1)
    # ----
    return corners

def corners_as_list():
    corners_list = corners.tolist() #list of lists. NOTE this goes 3 layers deep, with extraneous layer around coordinate pair.
    corners_sorted = sorted(corners_list)

# Lazy algorithm to get distance between two corner points. Assume all UV faces have same dimensions.
# Distance between two points = dimension for UV face.
# Sort distances in asscending order, to find smallest distance.
# TODO: represent as a tuple, with point 1, point 2 and distance.
# use Euclidean distance. (This works because perfect square. May not work for more complex shapes?)
# Lazy should definitely be my search key word for fixing sloppy code.
# PURPOSE: Find distance between all points. (Any two points.)
def find_distance(corners):
    distances = []

    i = 0
    j = 0
    # create list of all distances
    while i < len(corners):
        while j < len(corners):
            distances.append(np.linalg.norm(corners[i] - corners[j]))  # distance between first and second point
            j += 1
        j = 0
        i += 1
    distances.sort()
    # remove zeros from distances list
    i = 0
    count = 0
    while (distances[i] == 0.0) & (count < 50): #count added to avoid infinite loop
        distances.remove(0.0)
        count += 1

    # smallest non-zero value in distances is the distance of UV face's edge -- assuming all faces are identical squares, and mesh is a perfect cube.
    face_length = distances[0]
    return face_length

# CALL FUNCTIONS!
corners = find_corners()
face_len = find_distance(corners)


# DISPLAY!
cv.imshow('Original UV', uv_original)
# Harris
#cv.imshow('Harris', uv_harris)
#cv.imshow('Harris Corners', dst)
# Py Shi Tomasi
# cv.imshow('Py Shi Tomasi', corners) # Note: this doesn't work - can't show as image directly as output as array. Need to plot array.
cv.imshow('Py Shi Tomasi UV', uv_pyshitomasi)
plt.imshow(uv_pyshitomasi)

#print("Distances: ")
#print(distances)
print("UV Face Length: ")
print(face_len)
#print(corners)
#print("Corners unsorted list: ", corners_list)
#print("Corners sorted array:", corners_sorted)
#print("Corners type: ", type(corners))
#print("Distance between points: ", dist)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

# TODO: Handle cases where corner dectection is off by 2 pixels.
# TODO: Handle y coordinate sorting and corner artifact smoothing.
#TODO: distance between points must return integer. This all could likely be a function.
