import cv2
import pytesseract

img = cv2.imread('demo.png')
print(img)
img = cv2.resize(img, (640,480))
d = pytesseract.image_to_data(img)
print(d)

