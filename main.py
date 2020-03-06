import sitePMC
import funcoesBD

objDB = funcoesBD.dataBase("127.0.0.1", "sprint_user", "123456", "bancosprint0")

url = 'http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2'

objMogi = sitePMC.siteMogi(url)
objMogi.getTexto()

caracteres = ['{','[',']','"','servidores',',',':rgf:','rgf:','nome','cargo','rendimentos','.']

text = objMogi.filtraDados(caracteres)
servidorPublico = []

for i in range(0, len(text)):
    linha = text[i].split(":")
    if len(linha) == 4:
        servidorPublico.append((linha[0], linha[1], linha[2], linha[3]))
objDB.insertInTB(servidorPublico)