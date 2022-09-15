# edge detection

import cv2

#img = cv2.imread('Rectangles_0.png')
img = cv2.imread('Rectangles_1.png')
cv2.imshow("Rectangles", img)
cv2.waitKey(0)

#Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Blur image
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

cv2.imshow("blur", img_blur)
cv2.waitKey(0)


#Canny edge detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=230)
#edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=150)
#Display Canny edge detection image
cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite("Rectangles_1_Canny.png", edges)
cv2.waitKey(0)

