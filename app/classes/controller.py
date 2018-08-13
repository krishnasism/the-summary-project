import app.classes.scraper as scraper #scrape wikipedia  
import app.classes.summarizer as summarizer #summarize
import app.classes.image as image #summarize OCR
def generateSummary(topic):    
    try:
        #topic=input("Enter topic you want to search: ")
        text=scraper.scrape(topic) #scraped data
        #print(text) 
        summary=summarizer.summarize(text)
        #print(summary)
        return(summary)
        #summary=cleaner.clean(summary)
       # print(summary)
    except Exception as e:
        return(e)

#print(generateSummary('gay'))
        
def generateImageSummary(filename):
    try:
        summary=image.imageSumm(filename)
        return(summary)
    except Exception as e:
        return(e)