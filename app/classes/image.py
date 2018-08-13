def imageSumm(imageName):
    from PIL import Image
    import pytesseract
    import cv2
    import os
    import app.classes.summarizer as summarizer #summarize
    from nltk.tokenize import word_tokenize
    from autocorrect import spell
    import string
    # construct the argument parse and parse the arguments
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    
    # load the example image and convert it to grayscale
    image = cv2.imread(BASE_DIR+'\\static\\images\\'+imageName)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    


    filename = BASE_DIR+'\\static\\images\\1.png'.format(os.getpid())
    print(filename)
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    words = word_tokenize(text)
    print(words)
    text=""
    for word in words:
        if(word in string.punctuation):
            text+=word
        else:
            text+=" "+spell(word)
    print(text)
    summary=summarizer.summarize(text)
    print(text)
    print(summary)
    #os.remove(filename)
    return(summary)
    
