#10-08-2018 Krishnasis Mandal
#Downloading text from Wikipedia Page using Beautiful Soup
from bs4 import BeautifulSoup
import requests


##DATA FETCH FROM WIKIPEDIA
inp=input("Enter topic you want to search : ") #topic user wants to read about
response = requests.get("https://en.wikipedia.org/wiki/"+inp)
soup = BeautifulSoup(response.text,"lxml")
t = soup.find_all('p') #fetch <p></p> tags 


for i in range(0,len(t)):
    print(t[i].text) #display all text within <p> tags
    
##DATA FETCHED PREPROCESSING


