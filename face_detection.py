#!/usr/bin/env python

import os
import face_recognition as face
from PIL import Image, ImageDraw

for filename in os.listdir('sample_images'):
    img = face.load_image_file('sample_images/' + filename)
    face_locs = face.face_locations(img)
    pil_img = Image.fromarray(img)

    for face_loc in face_locs:
        t, r, b, l = face_loc

        draw = ImageDraw.Draw(pil_img)
        draw.line((r, t+5, l, t+5), fill=128, width=10)
        draw.line((r, t, r, b), fill=128, width=10)
        draw.line((r, b-4, l, b-4), fill=128, width=10)
        draw.line((l, t, l, b), fill=128, width=10)
        del draw

    pil_img.show()
