'''
    - 이미지 글자 추출 테스트
    cmd > tesseract path\name.png stdout

    - 패키지 설치
    pip install pillow
    pip install pytesseract
    pip install opencv-python
'''

import cv2
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# 설치한 tesseract 프로그램 경로 (64비트)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# 이미지 불러오기, Gray 프로세싱
#image = cv2.imread('C:\\Users\\IBK\\Desktop\\sample1.png')
image = cv2.imread('C:\\Users\\IBK\\Desktop\\sample2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장.
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Simple image to string
text = pytesseract.image_to_string(Image.open(filename), lang='eng')
os.remove(filename)

print(text)

cv2.imshow("Image", image)
cv2.waitKey(0)
