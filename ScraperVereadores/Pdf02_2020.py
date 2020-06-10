from tabula import read_pdf
import formatacaoNumeros as fn
from tabulate import tabulate
import pandas as pd

def LerPdf02(funcionarios):
    PdfFile = read_pdf("http://www.cmmc.com.br/siteadmin/downloads/arquivos/02.2020.pdf", pages='all', multiple_tables=True)
    PdfFile = pd.concat(PdfFile, ignore_index=True)
    print(tabulate(PdfFile))