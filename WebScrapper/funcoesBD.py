import pyodbc

class dataBase:
    def __init__(self, conectString):
        self.sqldb = pyodbc.connect(conectString)
        self.sqlCursor = self.sqldb.cursor()
    def insertManyInTB(self, listaDeTuplas, sqlComando):
        self.sqlCursor.executemany(sqlComando, listaDeTuplas)
        self.sqldb.commit()
