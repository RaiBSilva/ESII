import mysql.connector

class dataBase:
    def __init__(self, host, usuario, senha, schema):
        self.mydb = mysql.connector.connect(
            host=host,
            user=usuario,
            passwd=senha,
            database=schema
        )
        self.myCursor = self.mydb.cursor()
    def insertInTB(self, servidorPublico):
        self.sqlComando = "INSERT INTO servidores(rgf, nome_servidor, cargo_servidor, salario_servidor) VALUES (%s,%s,%s,%s)"
        self.myCursor.execute(self.sqlComando, servidorPublico)
        self.mydb.commit()