#10-08-2018 Krishnasis Mandal
#Downloading text from Wikipedia Page using Beautiful Soup
def scrape(topic):
    from bs4 import BeautifulSoup
    import requests
    
    ##DATA FETCH FROM WIKIPEDIA
    #topic=input("Enter topic you want to search : ") #topic user wants to read about
    response = requests.get("https://en.wikipedia.org/wiki/"+topic)
    soup = BeautifulSoup(response.text,"lxml")
    t = soup.find_all('p') #fetch <p></p> tags 
    
    text=""
    
    for i in range(0,len(t)):
        #print(t[i].text) #display all text within <p> tags
        text=text+t[i].text #add to corpus
    
    return(text)
#print(text)
    
##DATA FETCHED PREPROCESSING


