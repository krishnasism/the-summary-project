# -*- coding: utf-8 -*-
def crop(imageName):
    import cv2
    import os
    import numpy as np
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    image = cv2.imread(BASE_DIR+'\\static\\images\\best.jpg')
    #print(img)
    
    #grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #binary
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
     
    #dilation
    kernel = np.ones((1,1), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    
    #find contours
    im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    x1=0
    y1=0
    x2=0
    y2=0
    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
        if(i==0):
            x1=x
            y1=y
        # Getting ROI
        roi = image[y:y+h, x:x+w]
    #    if w > 0 and h > 0:
        if(x<x1):
             x1=x
        if(y<y1):
             y1=y
        if(y>y2):
             y2=y
        if(x>x2):
             x2=x
            #cv2.imwrite('C:\\Users\\Link\\Desktop\\output\\{}.png'.format(i), roi)
        # show ROI
        #cv2.imshow('segment no:'+str(i),roi)
        #cv2.rectangle(image,(x,y),( x + w, y + h ),(0,255,0),2)
        #cv2.waitKey(0)
    
    #cv2.rectangle(gray,(x1-10,y1-10),(x2+10,y2+10),(0,255,0),2)
    crop_img = gray[y1:y2+10, x1:x2+10]
    
    return crop_img