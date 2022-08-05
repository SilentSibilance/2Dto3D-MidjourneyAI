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
# Removed the need for these import lines by keeping directly as an opened opencv image.
#img0 = cv.imread("2-0.png")
#img1 = cv.imread("2-1.png")
#img2 = cv.imread("2-2.png")
#img3 = cv.imread("2-3.png")

def add_imgs_to_uv(name, images):

    img0 = images[0]
    img1 = images[1]
    img2 = images[2]
    img3 = images[3]


    print(img0.shape)
    # Check input image matches size of ROI. Resize if necessary. Assume you need to resize all images, as non-resized images will not end up modified anyways.
    img0_s = cv.resize(img0,(ROI_edge_length, ROI_edge_length))
    img1_s = cv.resize(img1,(ROI_edge_length, ROI_edge_length))
    img2_s = cv.resize(img2,(ROI_edge_length, ROI_edge_length))
    img3_s = cv.resize(img3,(ROI_edge_length, ROI_edge_length))

    # Rotate 4 faces images -90 degrees to appear upright on cube.
    # grab the dimensions of the image and calculate the center of the
    # image
    (h, w) = img3_s.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # rotate our image by -90 degrees around the image
    M = cv.getRotationMatrix2D((cX, cY), -90, 1.0)
    img0_s = cv.warpAffine(img0_s, M, (w, h))
    img1_s = cv.warpAffine(img1_s, M, (w, h))
    img2_s = cv.warpAffine(img2_s, M, (w, h))
    img3_s = cv.warpAffine(img3_s, M, (w, h))

    #cv.imshow("Rotated by -90 Degrees", rotated)

    # Note: We flip x and y coordinate. For some reason, needed.
    # Apply 4 MidjourneyAI images to 4 UV faces of cube.
    uv_img[2:256, 385:(639)] = img0_s
    uv_img[257:(257+ROI_edge_length), 385:(385+ROI_edge_length)] = img1_s
    uv_img[513:(513+ROI_edge_length), 385:(385+ROI_edge_length)] = img2_s
    uv_img[769:(769+ROI_edge_length), 385:(385+ROI_edge_length)] = img3_s

    uv_name = name + "_UV_w_textures.png"
    cv.imwrite(uv_name, uv_img)


#print(img0_s.shape)
