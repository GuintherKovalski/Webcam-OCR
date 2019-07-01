import pytesseract as ocr
from PIL import Image
import time
import nltk
from nltk.tokenize import word_tokenize
import cv2
import base64
import numpy as np 
import json
import numpy as np
#nltk.download()

def open_image(path):
    return Image.open(path) 

def img_to_text(source): 
    img = Image.fromarray(source, 'RGB')
    start = time.time()
    example_sent = ocr.image_to_string(img, lang='por')
    end = time.time()
    stop_words = nltk.corpus.stopwords.words('portuguese') 
    word_tokens = word_tokenize(example_sent)    
    text_out = []  
    for w in word_tokens: 
        if w not in stop_words: 
            text_out.append(w) 
    
    return example_sent, end - start
