def img():
    from PIL import Image
    from pytesseract import image_to_string
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    
    img = Image.open(BASE_DIR+'\\static\\images\\test.png')
    img.load()
    
    print(img)
    #img.show()
    
    
    #print (image_to_string(Image.open('testy.jpg')))
    return (image_to_string(Image.open(BASE_DIR+'\\static\\images\\test.png'), lang='eng'))