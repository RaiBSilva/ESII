import formatacaoNumeros as sp
from tabula import read_pdf
from tabulate import tabulate

PdfFile = read_pdf("http://www.cmmc.com.br/siteadmin/downloads/arquivos/04.2020.pdf", pages='all', multiple_tables=True)

funcionarios = []
for i in range(0, len(PdfFile[0])):
    nomeId = PdfFile[0].iloc[i, 0].split(maxsplit=1)
    cargoId = PdfFile[0].iloc[i, 1].split(maxsplit=1)
    funcionarios.append((nomeId[0], nomeId[1], cargoId[0], cargoId[1], PdfFile[0].iloc[i, 2], PdfFile[0].iloc[i, 3], PdfFile[0].iloc[i, 4], PdfFile[0].iloc[i, 5], PdfFile[0].iloc[i, 6], PdfFile[0].iloc[i, 7]))

for i in range(1,len(PdfFile)):
    tabela = PdfFile[i]
    colunas = tabela.columns
    funcionarios.append((sp.transformaInteiro(colunas[0]), colunas[1], colunas[2], colunas[3], colunas[4], colunas[5], colunas[6], colunas[7], colunas[8], colunas[9]))
    for row in range(0, len(PdfFile[i])):
        tupla = tabela.iloc[row]
        funcionarios.append((sp.transformaInteiro(tupla[0]), tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9]))

for i in funcionarios:
    print(i)



