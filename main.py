import requests
import lxml
from bs4 import BeautifulSoup

source = requests.get('http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2').text
soup = BeautifulSoup(source, 'lxml')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

dicionario = {}

for i in range(0, len(text)-1):
    if text[i] == '[':
        text = text.replace(text[i], "")
for i in range(0, len(text)-1):
    if text[i] == ']':
        text = text.replace(text[i], "")

""""for i in range(0, len(text)-1):
    if text[i] == '{':
        text = text.replace(text[i], "")"""


print(text)

""""x = text.split(",")
y = []
for i in x:
   y.append(i.split("{"))
for i in y:
   x.append(i.split("["))
print(x[0])"""

