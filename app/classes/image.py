from PIL import Image
import pytesseract
import os
import app.classes.summarizer as summarizer
import app.classes.preprocess as preprocess
from nltk.tokenize import word_tokenize
from autocorrect import spell
import string


def imageSumm(imageName: str) -> str:
    # Unused
    import cv2
    """
    Summarise images (WIP)
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = f"{BASE_DIR}\\static\\images\\{imageName}"
    gray = preprocess.crop(path)
    fileName = f"{BASE_DIR}\\static\\images\\1.png".format(os.getpid())

    cv2.imwrite(fileName, gray)

    text = pytesseract.image_to_string(Image.open(fileName))
    words = word_tokenize(text)

    text = ""
    for word in words:
        if (word in string.punctuation):
            text += word
        else:
            text += " "+spell(word)
    summary = summarizer.summarize(text)
    return summary
