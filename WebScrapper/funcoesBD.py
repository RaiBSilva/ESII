import pyodbc

class dataBase:
    def __init__(self, conectString):
        self.sqldb = pyodbc.connect(conectString)
        self.sqlCursor = self.sqldb.cursor()
    def insertInTBservidores(self, servidorPublico):
        try:
            self.sqlCursor.execute('DELETE servidores;')
            self.sqldb.commit()
        except:
            pass
        self.sqlComando = 'INSERT INTO servidores(rgf, nome_servidor, cargo_servidor, salario_servidor,salario_liquido_servidor,descontos_servidor) VALUES (?, ?, ?, ?, ?, ?);'
        self.sqlCursor.executemany(self.sqlComando, servidorPublico)
        self.sqldb.commit()

    def insertInTBremuneracao(self, remuneracao):
        try:
            self.sqlCursor.execute('DELETE remuneracao_servidores;')
            self.sqldb.commit()
        except:
            pass
        self.sqlComando = 'INSERT INTO remuneracao_servidores(rgf, nome_remuneracao, valor_remuneracao) VALUES (?, ?, ?);'
        self.sqlCursor.executemany(self.sqlComando, remuneracao)
        self.sqldb.commit()
    def insertInTBdescontos(self, desconto):
        try:
            self.sqlCursor.execute('DELETE descontos_servidores;')
            self.sqldb.commit()
        except:
            pass
        self.sqlComando = 'INSERT INTO descontos_servidores(rgf, nome_desconto, valor_desconto) VALUES (?, ?, ?);'
        self.sqlCursor.executemany(self.sqlComando, desconto)
        self.sqldb.commit()