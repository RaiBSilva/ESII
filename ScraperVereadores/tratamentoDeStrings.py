import re


def tiraQuebraLinhaInicial(lista):
    x = re.findall(r"\A\n", lista)
    if x:
        lista = lista[1:]
    y = re.findall(r"\n\b", lista)
    if y:
        lista = lista[:-1]
    return lista


def verificaString(string):
    string = string.replace(" ", "")
    try:
        string = string.replace("-", "")
    except:
        pass
    return string.isalpha()


def mergeLinhas(nome, linha):
    if nome[-1].strip() == '-':
        nome = nome.strip() + linha.strip()
    else:
        nome = nome.strip() + ' ' + linha.strip()
    return nome