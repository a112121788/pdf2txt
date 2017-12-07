from wand.image import Image
from wand.color import Color
import os
import re


def convert_pdf_to_jpg(filename):
    with Image(filename=filename, background=Color('White'), resolution=300) as img:
        print('pages = ', len(img.sequence))
        with img.convert('jpg') as converted:
            converted.alpha_channel = False
            converted.save(filename='input/page.jpg')

    resize_imgs('input')

def resize_imgs(dir):
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            file = os.path.join(parent, filename)
            m = re.search(r".jpg", str(file))
            if m:
                print(file)
                with Image(filename=file) as img:
                    r = 1024.0 / img.width
                    img.resize(int(img.width * r), int(img.height * r))
                    img.alpha_channel = False
                    img.save(filename=file)
