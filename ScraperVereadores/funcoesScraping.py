from bs4 import BeautifulSoup
import requests
import re


class Scraper:
    def __init__(self, url):
        self.source = requests.get(url).text
        self.soup = BeautifulSoup(self.source, 'lxml')

    def getlinks(self):
        links = []
        for link in self.soup.findAll('a', attrs={'href': re.compile("exibe_vereador")}):
            links.append(link.get('href'))
        return links
