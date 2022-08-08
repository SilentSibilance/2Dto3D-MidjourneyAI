# divide an image from MidjourneyAI into its 4 separate images.
# MidjourneyAI delivers a combined image of 4 sub images as a response to a prompt.
# Each image is cleanly located a one of the 4 respective corners.
#
import cv2 as cv
import numpy
print (cv.__version__)


#print (numpy._version)

# Note - Samples Images begins at '2'. This is an artifact of when I was downloading images, and the order they loaded on Discord. Not all images on the Discord are sets of 4. Some are single images.
img_path = 'red_room.png'
#img_path = 'sample-images/2.png'
img = cv.imread(img_path)
shape = img.shape
rows, cols, channels = shape
print(rows)
mid_rows = rows//2 # want floor division
mid_cols = cols//2

#print(mid_rows)
#print(mid_cols)
def separate_imgs():
    # Creates 4 separate images, from the respective 4 quadrants of the original image.
    img0 = img[0:mid_cols,0:mid_rows]
    img1 = img[mid_cols:cols,0:mid_rows]
    img2 = img[0:mid_cols,mid_rows:rows]
    img3 = img[mid_cols:cols,mid_rows:rows]

    # Write the 4 new images to directory.
    #cv.imwrite('2-0.png', img0)
    #cv.imwrite('2-1.png', img1)
    #cv.imwrite('2-2.png', img2)
    #cv.imwrite('2-3.png', img3)

    # Create a list of all images (without writing to the directory).
    images = [img0, img1, img2, img3]

    print('Converted to 4 images and saved.')

    return images

#TODO: Make code generic so can be fed any image. Or loops through all image names in a range.
