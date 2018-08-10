import scraper
import summarizer

topic=input("Enter topic you want to search: ")
text=scraper.scrape(topic)

print(text)

