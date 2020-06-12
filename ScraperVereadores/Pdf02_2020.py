import dadosPDF as dpdf
import requests

def LerPdf02():
    listaDeFuncionarios = []
    url = 'http://www.cmmc.com.br/siteadmin/downloads/arquivos/02.2020.pdf'
    arquivoPDF = requests.get(url)
    listaDePaginas = dpdf.lerPDF(arquivoPDF)
    listaDeFuncionarios = dpdf.filtraDados02_2020(listaDePaginas)
    listaDeFuncionarios = dpdf.organizaFuncionarios(listaDeFuncionarios)
    return listaDeFuncionarios