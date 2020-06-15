import io
from PyPDF2 import PdfFileReader
from tratamentoDeStrings import tiraQuebraLinhaInicial
from tratamentoDeStrings import verificaString
from tratamentoDeStrings import mergeLinhas


def lerPDF(arquivoPDF):
    f = io.BytesIO(arquivoPDF.content)
    reader = PdfFileReader(f)
    listaDePaginas = []
    for page in reader.pages:
        listaDePaginas.append(page.extractText())
    return listaDePaginas


def filtraDados02_2020(listaDePaginas):
    listaDeTabelas = []
    listaAuxiliar = []
    listaAuxiliar = listaDePaginas[0].split('LIQUIDO')
    listaAuxiliar = listaAuxiliar[1].split('Câmara Municipal de Mogi das Cruzes')
    listaDeTabelas.append(tiraQuebraLinhaInicial(listaAuxiliar[0]))
    for i in range(1, len(listaDePaginas)):
        listaAuxiliar = listaDePaginas[i].split('IRRF')
        listaAuxiliar = listaAuxiliar[1].strip()
        listaDeTabelas.append(tiraQuebraLinhaInicial(listaAuxiliar))
    return listaDeTabelas


def filtraDados04_2020(listaDePaginas):
    listaDeTabelas = []
    listaAuxiliar = []
    listaAuxiliar = listaDePaginas[0].split('LÍQUIDO')
    listaAuxiliar = listaAuxiliar[1].split("Referência")
    listaDeTabelas.append(tiraQuebraLinhaInicial(listaAuxiliar[0]))
    for i in range(1, len(listaDePaginas)):
        listaDeTabelas.append(tiraQuebraLinhaInicial(listaDePaginas[i].strip()))
    return listaDeTabelas


def organizaFuncionarios(list):
    listaOrganizada = []
    cont = 1
    tupla = []
    for i in range(0, len(list)):  # for responsável por passar as tabelas
        linhas = list[i].split('\n')  # faz uma lista com cada dado
        for linha in linhas:  # for responsável por passar as linhas
            if linha != "" and len(linha.strip()) >= 2:  # linhas vazias não serão consideradas
                if cont == 4:
                    if verificaString(linha):
                        tupla[-1] = mergeLinhas(tupla[-1], linha)
                        cont = cont - 1
                    else:
                        tupla.append(linha.strip())
                else:
                    tupla.append(linha.strip())
                cont = cont + 1
                if cont == 12:
                    cont = 1
                    listaOrganizada.append(tuple(tupla))
                    tupla = []
    return listaOrganizada


def organizaFuncionarios04_2020(list):
    listaOrganizada = []
    cont = 1
    tupla = []
    for i in range(0, len(list)): #for responsável por passar as tabelas
        linhas = list[i].split('\n') #faz uma lista com cada dado
        for linha in linhas: #for responsável por passar as linhas
            if linha != "":# linhas vazias não serão consideradas
                if cont == 5 or cont == 3:
                    if verificaString(linha):
                        tupla[-1] = mergeLinhas(tupla[-1],linha)
                        cont = cont - 1
                    else:
                        tupla.append(linha.strip())
                else:
                    tupla.append(linha.strip())
                cont = cont + 1
                if cont == 11:
                    cont = 1
                    listaOrganizada.append(tuple(tupla))
                    tupla = []
    return listaOrganizada
