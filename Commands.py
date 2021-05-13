import requests
import os
import numpy as np
import cv2
from skimage import io
import pytesseract


# pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\praty\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
class GetText:
    
    def text(Update, Context):
        print(str(Update.message.reply_to_message.photo[1].file_id))
        print(str(Update.message))
        receive = requests.get('https://api.telegram.org/bot'+os.environ['BOTTOKEN']+'/getFile?file_id='+str(Update.message.reply_to_message.photo[1].file_id))
        receive=receive.json()
        ffff= requests.get("https://api.telegram.org/file/bot"+os.environ['BOTTOKEN']+"/"+receive['result']['file_path'])
        print("https://api.telegram.org/file/bot"+os.environ['BOTTOKEN']+"/"+receive['result']['file_path'])
        img = io.imread("https://api.telegram.org/file/bot"+os.environ['BOTTOKEN']+"/"+receive['result']['file_path'])
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
        # cv2.imshow("jj", img)
        # cv2.waitKey()

        custom_config = r'--oem 3 --psm 6'
        Update.message.reply_text(pytesseract.image_to_string(img, config=custom_config))