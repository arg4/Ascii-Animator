# Quickly converts a given image to a json table of color values for ascii_animator.js
import json, os
from PIL import Image

full_array = []

def imageToJson(input_image, w, h):
    w_array = [];
    h_array = [];

    for hi in range(h):
        for wi in range(w):
            w_array.append(str(input_image[wi,hi]))
            #print(str(imported_image[wi,hi]))
        h_array.append(w_array)
        w_array = []

    return h_array


#image_2_decode = Image.open('little_arnie.png')# Image name goes here.

#imported_image = image_2_decode.load()

for filename in os.listdir('anim_2'):
    current_frame = Image.open('anim_2\\'+filename)
    frame_2_encode = current_frame.load()
    w = (current_frame.size[0])
    h = (current_frame.size[1])

    full_array.append(imageToJson(frame_2_encode, w, h))

with open('frames2.json', 'w') as outfile:
    outfile.write('frames =\'')
    outfile.write(str(json.dumps(full_array)))
    outfile.write('\';')

#print (str(h_array))
