# Shape detection
import cv2 as cv
import numpy as np


# Image pre-processing. Convert to greyscale, blur and threshold.
#img = cv.imread('3-2.png')
img = cv.imread('Rectangles_1_Canny.png')

#img_s = cv.resize(img,(100, 100)) # Resizing allows for cleaner gross shape detection
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
#thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1] # for high contrast backgrounds
thresh = cv.threshold(blurred, 40, 255, cv.THRESH_BINARY)[1] # for dark backgrounds - TODO: could ML tweak these values per image set. Could use multiple different thresholds to extract maximal information.

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Apply contour approximation to get gross shapes.
count = 0
print(type(contours))
#approx = np.ones_like(contours, dtype=object)
contours_array = np.asarray(contours, dtype=object)
approx = np.copy(contours_array)  # Conversion from type Tuple to type np.Array required for contours.
print("Contours array: ")
print(contours)
for cnt in contours:
    epsilon = 0.05*cv.arcLength(cnt,True)
    approx[count] = cv.approxPolyDP(cnt,epsilon,True)
    count += 1


# Draws the contours back onto original image.
cv.drawContours(img, approx, -1, (0,255,0), 3)
# Draws the contours onto a blank new image.

#cv.imwrite('3-2-c-approx.png', img)
cv.imwrite('Rectangles_1_w_curves_tree.png', img)


# Rectangle detection aka. building detection
