import sitePMC

url = 'http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2'

objMogi = sitePMC.siteMogi(url)
objMogi.getTexto()

caracteres = ['{','[',']','"','servidores',',',':rgf:','rgf:','nome','cargo','rendimentos']

text = objMogi.filtraDados(caracteres)

for i in text:
    print(i + "\n")