import scraper #scrape wikipedia  
import summarizer #summarize

topic=input("Enter topic you want to search: ")
text=scraper.scrape(topic) #scraped data
#print(text) 
summary=summarizer.summarize(text)
print(summary)


