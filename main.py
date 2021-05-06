import pytesseract as tsc
import time
import os

tsc.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
ruta = r'D:\tesseract\img'

lista = os.listdir(ruta)

for elemento in lista:
    if elemento.split('.')[-1] in ('png', 'jpg', 'jpeg', 'tiff'):
        texto = tsc.image_to_string(
            ruta+'\\'+elemento, config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')
        print(texto)
