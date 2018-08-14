def crop(path):
    import cv2
    import numpy as np
    
    
    image = cv2.imread(path)
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
     
    kernel = np.ones((1,1), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    
    im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
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

        if(x<x1):
             x1=x
        if(y<y1):
             y1=y
        if(y>y2):
             y2=y
        if(x>x2):
             x2=x
          
    crop_img = gray[y1:y2+10, x1:x2+10]
    
    return crop_img