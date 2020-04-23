import pyodbc

class dataBase:
    def __init__(self, conectString):
        self.sqldb = pyodbc.connect(conectString)
        self.sqlCursor = self.sqldb.cursor()

    def execProcedureTruncateTables(self):
        self.sqlCursor.execute('EXEC dbo.truncateTables;')
        self.sqldb.commit()

    def insertManyInTB(self, listaDeTuplas, sqlComando):
        self.sqlCursor.executemany(sqlComando, listaDeTuplas)
        self.sqldb.commit()