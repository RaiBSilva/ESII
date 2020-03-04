from sitePMC import getTexto
from sitePMC import filtraDados

url = 'http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2'

text = getTexto(url)
print(text)
caracteres = ['{','[',']','"','servidores',',',':rgf:','rgf:','nome','cargo','rendimentos']
text = filtraDados(caracteres, text)

for i in text:
    print(i + "\n")