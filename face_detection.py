#!/usr/bin/env python

import os
import face_recognition as face
from PIL import Image, ImageDraw

if __name == '__main__':
    for filename in os.listdir('sample_images'):
        img = face.load_image_file('sample_images/' + filename)
        face_locs = face.face_locations(img)
        pil_img = Image.fromarray(img)

        for face_loc in face_locs:
            t, r, b, l = face_loc
            mid = (r+l) / 2
            upperLip = b-((b-t) / 3)
            print t, b, upperLip

            draw = ImageDraw.Draw(pil_img)
            draw.line((mid-15, upperLip, mid+15, upperLip), fill=128, width=10)
            draw.line((r, t+5, l, t+5), fill=128, width=10)
            draw.line((r, t, r, b), fill=128, width=10)
            draw.line((r, b-4, l, b-4), fill=128, width=10)
            draw.line((l, t, l, b), fill=128, width=10)
            del draw

        pil_img.show()
