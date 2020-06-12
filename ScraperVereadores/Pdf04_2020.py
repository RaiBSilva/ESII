import requests
import dadosPDF as dpdf

def LerPdf04():
    listaDeFuncionarios = []
    url = 'http://www.cmmc.com.br/siteadmin/downloads/arquivos/04.2020.pdf'
    arquivoPDF = requests.get(url)
    listaDePaginas = dpdf.lerPDF(arquivoPDF)
    listaDeFuncionarios = dpdf.filtraDados04_2020(listaDePaginas)
    listaDeFuncionarios = dpdf.organizaFuncionarios04_2020(listaDeFuncionarios)
    return listaDeFuncionarios