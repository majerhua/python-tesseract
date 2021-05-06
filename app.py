import os
from PIL import Image

import pytesseract
captcha = pytesseract.image_to_string(Image.open(
    'captcha.jpg'), config='-psm 8 -c tessedit_char_whitelist=0123456789abcdfghijkmnlopqrsturstuvwxyz')
captcha = captcha.replace(" ", "").strip()
print(captcha)
