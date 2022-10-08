import app.classes.scraper as scraper
import app.classes.summarizer as summarizer
import app.classes.image as image
import logging

def generateSummary(input: str, text_summary: bool) -> str:
    """
    Get summary of a topic
    """
    try:
        if text_summary:
            text = input
        else:
            text = scraper.scrape(input)
        summary = summarizer.summarize(text)
        return summary
    except Exception as e:
        logging.error(e)
        return ["Sorry, we were unable to process your request"]


def generateImageSummary(filename: str) -> str:
    try:
        summary = image.imageSumm(filename)
        return summary
    except Exception as e:
        logging.error(e)
        return ""
