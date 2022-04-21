import requests
from bs4 import BeautifulSoup

url ="https://www.google.com"

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Chrome/72.0.3626.121"
}


def webscraper(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    return soup

for item in webscraper(url).find_all("div", class_ = "gb_Hd"):
    print(item.text)

for item in webscraper(url).find_all("img"):
    print(item.get("alt"))
    print(item.get("src"))