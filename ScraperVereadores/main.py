from tabula import read_pdf
import pandas as pd

PdfFile = read_pdf("http://www.cmmc.com.br/siteadmin/downloads/arquivos/04.2020.pdf", pages='all', multiple_tables=True)

# for i in PdfFile:
#     for index, row in i.iterrows():
#         print(index, row)
# aux = 1
# tab1 = []
# idParlamentar = 0
tabela = PdfFile[0]
for i in range(0,1):
    print(tabela.iloc[i,1])
    print(type(tabela.iloc[i, 1]))
    print(tabela.iloc[i,1].split(maxsplit=1))

# colunas = PdfFile[1].columns
# print(colunas[0])
# print(type(colunas))

# tab1.append(idParlamentar, nome, idCargo, cargo, vencimentoBase, outrosVencimentos, previdencia, irrf, outrosDescontos, liquido)
