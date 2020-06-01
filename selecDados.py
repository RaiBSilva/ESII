import re

def pegaDados(conteudoPDF):
	textoComp = conteudoPDF
	textoComp = textoComp.replace("�","*")
	textoComp = textoComp.split("Di*rias Pagas")
	listaFinal = []
	for indice in textoComp:

		ergf = re.findall(r'ERGF\n+(.*)',indice,flags=re.I)

		if(ergf != []):
			ergf = ergf[0].replace(".","")
			ergf = ergf[1]+ergf[2]+ergf[3]+ergf[4]+ergf[5]
			# print(ergf)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			saida = indice.split('Sa*da')
			saida = saida[1]
			saida = saida.split("Chegada")

			chegada = saida[1]
			saida = saida[0]

			DataSaida = re.findall(r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})',saida,flags=re.I)
			# print(DataSaida)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			DataChegada = chegada.split("Data Digita**o")
			DataChegada = DataChegada[0]
		

			DataChegada = re.findall(r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})',DataChegada,flags=re.I)
			if(DataChegada == []):
				DataChegada = ["","00-00-0000",""]
			# print(DataChegada)	
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			CidadeDestino = saida.split("Cidade de Destino")
			if(len(CidadeDestino)>1):
				CidadeDestino = CidadeDestino[1]
				CidadeDestino = CidadeDestino.split("Motivo")
				CidadeDestino = CidadeDestino[0]

				CidadeDestino = CidadeDestino.splitlines()
				
				if(len(CidadeDestino)<3):
					CidadeDestino = ["","Não encontrada",""]

				# print(CidadeDestino)
			else:
				CidadeDestino = ["","Não encontrada",""]
				# print(CidadeDestino)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			Motivo = saida.split("Motivo")
			if(len(Motivo)>1):
				Motivo = Motivo[1]
				if "Nome" in Motivo:
					Motivo = Motivo.split("Nome")
					Motivo = Motivo[0]
				if "Depto/Divis*o" in Motivo:
					Motivo = Motivo.split("Depto/Divis*o")
					Motivo = Motivo[0]

				Motivo = Motivo.splitlines()

				if(len(Motivo)<3):
					Motivo = ["","Não encontrada",""]

				# print(Motivo)
			else:
				Motivo = ["","Não encontrada",""]
				# print(Motivo)
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			valor = chegada.replace("$", "S")
			
			valor = re.findall(r'RS([0-9]{1,5}\,[0-9]{2})',valor,flags=re.I)
			# print(valor)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
			
			if(len(valor) == 1):
				DataChegada = DataChegada[0].replace("/","-")
				DataSaida = DataSaida[0].replace("/","-")
				valor = valor[0].replace(",",".")

				listaFinal.append((int(ergf),DataSaida,DataChegada,CidadeDestino[1],Motivo[1],float(valor)))
			else:
				cont1 = 0
				cont2 = 1
				cont3 = 2
				while cont1 < len(valor):

					DataSaidaAux = DataSaida[cont1].replace("/","-")

					if(DataChegada[1] == "00-00-0000"):
						DataChegadaAux = DataChegada[1]
					else:
						DataChegadaAux = DataChegada[cont1].replace("/","-")


					if(CidadeDestino[1] == ''):
						CidadeDestinoAux = CidadeDestino[cont3]
						cont3 += 1
					elif(CidadeDestino[1] == "Não encontrada"):
						CidadeDestinoAux = CidadeDestino[1]
					else:
						CidadeDestinoAux = CidadeDestino[cont2]


					valorAux = valor[cont1].replace(",",".")


					if(Motivo[1] == "Não encontrada"):
						MotivoAux = Motivo[1]
					else:
						MotivoAux = Motivo[cont2]

					
					cont1 += 1
					cont2 += 1
					
					listaFinal.append((int(ergf),DataSaidaAux,DataChegadaAux,CidadeDestinoAux,MotivoAux,float(valorAux)))


	return listaFinal