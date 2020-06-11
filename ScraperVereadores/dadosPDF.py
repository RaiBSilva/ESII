import io
from PyPDF2 import PdfFileReader
import formatacaoNumeros

def verificaString(string):
    string = string.replace(" ", "")
    try:
        string = string.replace("-", "")
    except:
        pass
    return string.isalpha()

def lerPDF(arquivoPDF):

    f = io.BytesIO(arquivoPDF.content)
    reader = PdfFileReader(f)
    listaDePaginas = []
    for page in reader.pages:
        listaDePaginas.append(page.extractText())
    return listaDePaginas

def filtraDados(listaDePaginas):
    listaDeTabelas = []
    listaAuxiliar = []
    listaAuxiliar = listaDePaginas[0].split('LIQUIDO')
    listaAuxiliar = listaAuxiliar[1].split('Câmara Municipal de Mogi das Cruzes')
    listaDeTabelas.append(listaAuxiliar[0])
    for i in range(1, len(listaDePaginas)):
        listaAuxiliar = listaDePaginas[i].split('IRRF')
        listaAuxiliar = listaAuxiliar[1].strip()
        listaAuxiliar = listaAuxiliar.rstrip('\n')
        listaDeTabelas.append(listaAuxiliar)
    return listaDeTabelas

def organizaFuncionarios(list):
    listaOrganizada = []
    cont = 1
    ergf =''
    nome = ''
    cargo = ''
    vencBase = ''
    outrosVenc = ''
    totalBruto = ''
    previdencia = ''
    irrf = ''
    outrosDescont = ''
    totalDescont = ''
    liquido = ''
    for i in range(0, len(list)): #for responsável por passar as tabelas
        linhas = list[i].split('\n') #faz uma lista com cada dado
        for linha in linhas: #for responsável por passar as linhas
            if cont == 1:
                ergf = linha
            elif cont == 2:
                nome = linha
            elif cont == 3:
                cargo = linha
            elif cont == 4:
                if verificaString(linha):
                    cargo = cargo + linha
                    cont = cont - 1
                else:
                    vencBase = linha
            elif cont == 5:
                outrosVenc = linha
            elif cont == 6:
                totalBruto = linha
            elif cont == 7:
                previdencia = linha
            elif cont == 8:
                irrf = linha
            elif cont == 9:
                outrosDescont = linha
            elif cont == 10:
                totalDescont = linha
            elif cont == 11:
                liquido = linha
            cont = cont + 1
            if cont == 12:
                cont = 1
                listaOrganizada.append((ergf, nome, cargo, vencBase, outrosVenc, totalBruto, previdencia, irrf, outrosDescont, totalDescont, liquido))
    return listaOrganizada