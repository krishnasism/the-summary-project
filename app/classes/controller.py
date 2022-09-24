import app.classes.scraper as scraper
import app.classes.summarizer as summarizer
import app.classes.image as image


def generateSummary(topic: str) -> str:
    """
    Get summary of a topic
    """
    try:
        text = scraper.scrape(topic)
        summary = summarizer.summarize(text)
        return summary
    except Exception as e:
        return (str(e))


def generateImageSummary(filename: str) -> str:
    try:
        summary = image.imageSumm(filename)
        return (summary)
    except Exception as e:
        return (str(e))
