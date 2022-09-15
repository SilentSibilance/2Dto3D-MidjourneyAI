# Generate a simple image of rectangles with known coordinates, to use as a bypass for the image detection step.

from PIL import Image, ImageDraw

#create an image object
img = Image.new('RGB', (400, 400), (80, 80, 80))
#create a draw object
draw = ImageDraw.Draw(img)
draw.rectangle((40, 120, 120, 320), fill=(210, 210, 210), outline=(255, 255, 255))

img.save("bypass_0.png")
