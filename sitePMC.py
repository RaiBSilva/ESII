import requests
from bs4 import BeautifulSoup
class siteMogi:
    def __init__(self, url):
        self.source = requests.get(url).text
        self.soup = BeautifulSoup(self.source, 'lxml')
    def getTexto(self):
        # kill all script and style elements
        for script in self.soup(["script", "style"]):
            script.extract()  # rip it out
        # get text
        self.text = self.soup.get_text()
        # break into lines and remove leading and trailing space on each
        self.lines = (line.strip() for line in self.text.splitlines())
        # break multi-headlines into a line each
        self.chunks = (phrase.strip() for line in self.lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in self.chunks if chunk)

    def filtraDados(self, caracteres):
        for i in range(0, len(caracteres)):
            self.text = self.text.replace(caracteres[i], "")
        self.text = self.text.split("}")
        return self.text