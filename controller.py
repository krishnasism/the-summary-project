import scraper #scrape wikipedia  
import summarizer #summarize
try:
    topic=input("Enter topic you want to search: ")
    text=scraper.scrape(topic) #scraped data
    #print(text) 
    summary=summarizer.summarize(text)  
    print(summary)
    #summary=cleaner.clean(summary)
   # print(summary)
except Exception as e:
    print("Error while parsing data\n")
    print(e)