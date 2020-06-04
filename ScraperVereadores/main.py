import funcoesScraping
import funcoesBanco


pointerScraper = funcoesScraping.Scraper('http://www.cmmc.com.br/vereadores/')
finalLink = pointerScraper.getlinks()
linkCompleto = []

for chunk in finalLink:
    linkCompleto.append('http://www.cmmc.com.br/vereadores/' + chunk)
for i in linkCompleto:
    print(i)