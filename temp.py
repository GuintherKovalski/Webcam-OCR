import cv2
import convert
import numpy as np
import time
from PIL import Image
#img = cv2.imread('page-1.png')
cap = cv2.VideoCapture(0)
itters = 0
while True:
   
    ret, frame = cap.read()
    cv2.imshow('OCR',frame)
    texto, tempo = convert.img_to_text(frame)
    if itters == 50:
        print(texto)
        itters = 0
    itters+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()


#img  = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
#a = cv2.fastNlMeansDenoisingColored(frame)
#img  = cv2.fastNlMeansDenoisingColored(frame,None,4,50,10,10)
#sobelx8u = cv2.Sobel(img,cv2.CV_8U,2,0,ksize=3)
#Image.fromarray(sobelx8u, 'RGB')
#img = Image.fromarray(img, 'RGB')
#texto, tempo = convert.img_to_text(sobelx8u)


