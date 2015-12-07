# Python 3.4
from bs4 import BeautifulSoup
import urllib.request
import requests

def scrape_imgur():
    category = input("Enter search criteria: ").replace(' ','+')
    url = "http://imgur.com/search/score?q=" + category
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    count = 0
    
    for link in soup.find_all('img'):
        picture_url = link.get('src')[2:]
        if picture_url[0] == 'i':
            count += 1
            picture_url = 'http://' + picture_url
            f = open('{0}.jpg'.format(count),'wb')
            f.write(requests.get(picture_url).content)
            f.close()
scrape_imgur()
