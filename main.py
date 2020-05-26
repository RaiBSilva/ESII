# -----------------------------------------------------------------------------------------
# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from urllib.request import urlopen

# def lerPDF(arquivoPDF):
#     # PDFResourceManager Usado para armazenar recursos compartilhados
#     # como fontes e imagens
#     recursos = PDFResourceManager()
#     buffer = StringIO()
#     layoutParams = LAParams()
#     dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
#     process_pdf(recursos, dispositivo, arquivoPDF)
#     dispositivo.close()
#     conteudo = buffer.getvalue()
#     buffer.close()
#     return conteudo

# arquivoPDF = urlopen("http://www.transparencia.pmmc.com.br/docs/diarias022020.pdf")
# stringSaida = lerPDF(arquivoPDF)
# # print(stringSaida)

# arquivoTxt = open("teste.txt","w", encoding="utf-8")
# arquivoTxt.write(stringSaida)
# arquivoTxt.close()

# arquivoPDF.close()
# ----------------------------------------------------------------------------------------
import re

arquivoTxt = open('teste.txt','r', encoding="utf-8")
teste = arquivoTxt.read()
# print(teste)
arquivoTxt.close()

teste = teste.split("Di�rias Pagas")
# print(teste)

for i in teste:
	# print(i)

# print(teste)

	RegInicial = re.findall(r'Escala:\s?(.*)\n+ERGF\n+(.*)\n+m.s\sescala\n+(.{0,2})\n+Unidade\n+(.*)\n+Cargo/Fun..o\n+(.*)\n+Despacho Secret.rio\n+(.*)\n+(.*)\n+Detalhamento\n+Nome\n+(.*)\n+Ano Escala\n+(.*)\n+Depto/Divis.o\n+(.*)\n+Valor Total\n+(.*)\n+Secret.rio\n+(.*)\n+Secretaria\n+(.*)\n+Situa..o\n+(.*)\n+Data Despacho Secret.rio\n+(.*)\n+Sa.da\n+Data',i,flags=re.I)
	if(RegInicial != []):
		# print(RegInicial)

		# ---------------Saida-------------------
		tabela = i.split('Sa�da')
		tabela = tabela[1]
		tabela = tabela.split("Chegada")

		# # print(tabela[0])

		# Indice = tabela[0].split("Data")
		# Indice = Indice[1]
		# Indice = Indice.split("Hor�rio")
		
		# DataSaida = Indice[0]
		# DataSaida = DataSaida.splitlines()
		# print(DataSaida)

		# Indice = Indice[1]
		# Indice = Indice.split("Cidade de Destino")

		# HorarioSaida = Indice[0]
		# HorarioSaida = HorarioSaida.splitlines()
		# print(HorarioSaida)

		# Indice = Indice[1]
		# Indice = Indice.split("Motivo")

		# CidadeDestino = Indice[0]
		# CidadeDestino = CidadeDestino.splitlines()
		# print(CidadeDestino)

		# Motivo = Indice[1]
		# Motivo = Motivo.splitlines()
		# print(Motivo)
		# ---------------Saida-------------------

		# ---------------Chegada-------------------
		Indice = tabela[1].split("Data")
		Indice = Indice[1]
		Indice = Indice.split("Hor�rio")


		DataChegada = Indice[0]
		DataChegada = DataChegada.splitlines()
		print(DataChegada)

		HorarioChegada = Indice[1]
		HorarioChegada = HorarioChegada.splitlines()
		print(HorarioChegada)


		Indice = tabela[1].split("Data Digita��o")
		Indice = Indice[1]
		Indice = Indice.split("Valor")


		DataDigitacao = Indice[0]
		DataDigitacao = DataDigitacao.splitlines()
		print(DataDigitacao)

		Indice = Indice[1]
		Indice = Indice.split("Chefia Imediata")

		indAux = Indice[0]
		indAux = re.findall(r'([0-9\,R$]+)\s(.*)',indAux,flags=re.I)
		DespachoChefia = []
		valor = []
		cont = 0
		while cont < len(indAux):
			DespachoChefia.append(indAux[cont][1])
			valor.append(indAux[cont][0])
			cont += 1

		# indAux = indAux.splitlines()
		print(valor)
		print(DespachoChefia)

		Indice = Indice[1]
		Indice = Indice.split("Data Despacho Chefia")

		chefiaImediata = Indice[0]
		chefiaImediata = chefiaImediata.splitlines()
		print(chefiaImediata)

		dataDespChefia = Indice[1]
		dataDespChefia = re.findall(r'([0-9\/]{10})',dataDespChefia,flags=re.I)
		print(dataDespChefia)

		
		# ---------------Chegada-------------------

	# print(re.findall(r'Data',teste[0],flags=re.I))

# print(re.findall(r'Data\n+(.+\n*)',teste,flags=re.I))


