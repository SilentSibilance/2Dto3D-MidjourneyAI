# Main file

import argparse

import quarter_image
import gen_texture

#TODO convert each of the scripts to using functions
# Create an image name input from command line.
# Clean up and automate handling of images.
# Keep images as imimage, not saved as separate pngs.

# Ask user for image name input and parse the input.
parser = argparse.ArgumentParser()
parser.add_argument('foo', type = str, help = 'Input the file name of the MidjourneyAI image you wish to process.')
#args = parser.parse_args()

#new_name = args.foo
#print(new_name)

#name = "turtle"

#images = quarter_image.separate_imgs()
#gen_texture.add_imgs_to_uv(name, images)

