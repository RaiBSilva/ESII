import dadosPDF as dpdf
import requests

def LerPdf02():
    url = 'http://www.cmmc.com.br/siteadmin/downloads/arquivos/02.2020.pdf'
    arquivoPDF = requests.get(url)
    listaDePaginas = dpdf.lerPDF(arquivoPDF)
    listaDeFuncionarios = dpdf.filtraDados(listaDePaginas)
    print(listaDeFuncionarios)
    # listaDeFuncionarios = dpdf.organizaFuncionarios(listaDeFuncionarios)
    # for i in listaDeFuncionarios:
    #     print(i)