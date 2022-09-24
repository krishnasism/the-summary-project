def scrape(topic: str) -> str:
    """
    Scrape wikipedia
    """
    from bs4 import BeautifulSoup
    import requests

    # DATA FETCH FROM WIKIPEDIA
    response = requests.get("https://en.wikipedia.org/wiki/"+topic)
    soup = BeautifulSoup(response.text, "lxml")
    t = soup.find_all('p') 

    text = ""

    for i in range(0, len(t)):
        text += t[i].text 

    return text
