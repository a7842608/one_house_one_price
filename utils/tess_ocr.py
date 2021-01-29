import re

import pytesseract
from PIL import Image


class OcrImageView(object):
    '''ocr'''

    def __init__(self, path):
        self.image = Image.open(path)
        self.text = pytesseract.image_to_string(self.image)

    def __str__(self):
        return self.text


if __name__ == '__main__':
    pass
