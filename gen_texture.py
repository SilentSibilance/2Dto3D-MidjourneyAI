# Generate a texture file for the 3D mesh, off of the UV.
# Currently assuming a perfect cube.


# input uv base map
# input 1-6 Images

# output texture file as png


# Hardcode ROIs for now.
# TODO: autodetect top-left corner for each square ROI.

# ROI top-left corner: (129, 257), (385, 2), (385, 257), (385, 511), (385, 769), (639, 257)
# ROI edge length: 251 px (from uv_detect_smallest_distance.py)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

ROI_edge_length = 254
ROI_offset = [(129, 257), (385, 2), (385, 257), (385, 513), (385, 769), (639, 257)]

uv_img = cv.imread("Cube_UV_condensed.png")
img0 = cv.imread("2-0.png")
img1 = cv.imread("2-1.png")
img2 = cv.imread("2-2.png")
img3 = cv.imread("2-3.png")

print(img0.shape)
# Check input image matches size of ROI. Resize if necessary. Assume you need to resize all images, as non-resized images will not end up modified anyways.
img0_s = cv.resize(img0,(ROI_edge_length, ROI_edge_length))
img1_s = cv.resize(img1,(ROI_edge_length, ROI_edge_length))
img2_s = cv.resize(img2,(ROI_edge_length, ROI_edge_length))
img3_s = cv.resize(img3,(ROI_edge_length, ROI_edge_length))

# Note: We flip x and y coordinate. For some reason, needed.
# Apply 4 MidjourneyAI images to 4 UV faces of cube.
uv_img[257:(257+ROI_edge_length), 129:(129+ROI_edge_length)] = img0_s
uv_img[2:256, 385:(639)] = img1_s
uv_img[257:(257+ROI_edge_length), 385:(385+ROI_edge_length)] = img2_s
uv_img[513:(513+ROI_edge_length), 385:(385+ROI_edge_length)] = img3_s

cv.imwrite('Cube_UV_w_textures.png', uv_img)


print(img0_s.shape)
