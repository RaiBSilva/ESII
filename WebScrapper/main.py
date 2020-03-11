import sitePMC
import funcoesBD

objDB = funcoesBD.dataBase("DSN=abc;Server=localhost\sqlexpress;Database=sprint0;Trusted_connection=yes;")

url = 'http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2'

objMogi = sitePMC.siteMogi(url)
objMogi.getTexto()

caracteres = ['{','[',']','"','servidores',',',':rgf:','rgf:','nome','cargo','rendimentos','.']

text = objMogi.filtraDados(caracteres)
servidorPublico = []

for i in range(0, len(text)):
    linha = text[i].split(":")
    if len(linha) == 4:
        salario = float(linha[3])/100
        salario = "%.2f" %salario
        servidorPublico.append((linha[0], linha[1], linha[2], salario))

objDB.insertInTB(servidorPublico)
