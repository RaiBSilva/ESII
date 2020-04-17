import requests
from bs4 import BeautifulSoup
import json


def convertint(str):
    try:
        str = str.replace('.', '')
    except:
        pass
    str = str.replace(',', '.')
    return float(str)


class siteMogi:
    def __init__(self, url):
        self.source = requests.get(url).text
        self.soup = BeautifulSoup(self.source, 'lxml')

    def getTexto(self):
        self.text = self.soup.get_text()
        return self.text

    def extraiRGF(self,texto):
        self.jon = json.loads(texto)
        rgfs = []
        for servidor in self.jon['servidores']:
            rgfs.append(servidor['rgf'])
        return rgfs

    def extraiDetalhamento(self,texto,rgf):
        salario = 0
        salLiquido = 0
        descontos = 0
        self.data = json.loads(texto)
        for info in self.data['totais']:
            aux = info['nome'].strip()
            if aux == 'TOTAL VENCIM/TO':
                salario = convertint(info['valor'])
            elif aux == 'TOTAL LIQUIDO':
                salLiquido = convertint(info['valor'])
            elif aux == 'TOTAL DESCONTOS':
                descontos = convertint(info['valor'])
        detalhamento =(rgf, self.data['nome'], self.data['cargo'], salario, salLiquido, descontos)
        return detalhamento

    def extraiRendimentos(self,rgf):
        rendimentos = []
        for info in self.data['rendimentos']:
            rendimentos.append((rgf, info['nome'].strip(), convertint(info['valor'])))
        return rendimentos

    def extraiDescontos(self,rgf):
        descontos = []
        for info in self.data['descontos']:
            descontos.append((rgf, info['nome'].strip(), convertint(info['valor'])))
        return descontos

    def organizaLista(self, remuneracao):
        listaOrganizada = []
        for i in remuneracao:
            for y in i:
                listaOrganizada.append(y)
        return listaOrganizada