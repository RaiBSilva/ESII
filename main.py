import dadosPDF
import selecDados
from urllib.request import urlopen
import pyodbc

sqldb = pyodbc.connect("DSN=SQLEXPRESS;Server=localhost\sqlexpress;Database=Se_Liga_Mogi;Trusted_connection=yes;")
sqlCursor = sqldb.cursor()

arquivoPDF = urlopen("http://www.transparencia.pmmc.com.br/docs/diarias022020.pdf")
stringSaida = dadosPDF.lerPDF(arquivoPDF)
arquivoPDF.close()

# arquivoTxt = open("teste.txt","w", encoding="utf-8")
# arquivoTxt.write(stringSaida)
# arquivoTxt.close()


# arquivoTxt = open("teste.txt","r", encoding="utf-8")
# stringSaida = arquivoTxt.read()
# arquivoTxt.close()





# print(stringSaida)

lista = selecDados.pegaDados(stringSaida)

print(lista)
# sqlCursor.executemany('INSERT INTO diarias_e_passagens(rgf, data_inicio, data_fim, destino,motivo,valor) VALUES (?, ?, ?, ?, ?, ?);', lista)
# sqldb.commit()