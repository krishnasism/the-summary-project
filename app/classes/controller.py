import app.classes.scraper as scraper
import app.classes.summarizer as summarizer
import app.classes.image as image
import logging

def generateSummary(topic: str) -> str:
    """
    Get summary of a topic
    """
    try:
        text = scraper.scrape(topic)
        summary = summarizer.summarize(text)
        return summary
    except Exception as e:
        logging.error(e)
        return ""


def generateImageSummary(filename: str) -> str:
    try:
        summary = image.imageSumm(filename)
        return summary
    except Exception as e:
        logging.error(e)
        return ""
