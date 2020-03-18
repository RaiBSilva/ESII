import pyodbc

class dataBase:
    def __init__(self, conectString):
        self.sqldb = pyodbc.connect(conectString)
        self.sqlCursor = self.sqldb.cursor()
    def insertInTB(self, servidorPublico):
        try:
            self.sqlCursor.execute("TRUNCATE TABLE servidores;")
        except:
            print("Tabela ja vazia")
            
        self.sqlComando = 'INSERT INTO servidores(rgf, nome_servidor, cargo_servidor, salario_servidor) VALUES (?, ?, ?, ?);'
        self.sqlCursor.executemany(self.sqlComando, servidorPublico)
        self.sqldb.commit()
