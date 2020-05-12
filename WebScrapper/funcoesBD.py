import pyodbc

class dataBase:
    def __init__(self, conectString):
        self.sqldb = pyodbc.connect(conectString)
        self.sqlCursor = self.sqldb.cursor()

    def execTruncateTables(self):
        self.sqlCursor.execute('alter table dbo.descontos_servidores drop constraint FK_descontos_servidores_servidores;')
        self.sqlCursor.execute('alter table dbo.remuneracao_servidores drop constraint FK_remuneracao_servidores_servidores;')
        self.sqlCursor.execute('alter table dbo.diarias_e_passagens drop constraint FK_diarias_e_passagens_servidores;')
        self.sqlCursor.execute('truncate table dbo.servidores;')
        self.sqlCursor.execute('truncate table dbo.descontos_servidores;')
        self.sqlCursor.execute('truncate table dbo.remuneracao_servidores;')
        self.sqlCursor.execute('truncate table dbo.diarias_e_passagens;')
        self.sqlCursor.execute('ALTER TABLE dbo.descontos_servidores WITH CHECK ADD CONSTRAINT FK_descontos_servidores_servidores FOREIGN KEY (rgf) REFERENCES dbo.servidores(rgf);')
        self.sqlCursor.execute('ALTER TABLE dbo.remuneracao_servidores WITH CHECK ADD CONSTRAINT FK_remuneracao_servidores_servidores FOREIGN KEY (rgf) REFERENCES dbo.servidores(rgf);')
        self.sqlCursor.execute('ALTER TABLE dbo.diarias_e_passagens WITH CHECK ADD CONSTRAINT FK_diarias_e_passagens_servidores FOREIGN KEY (rgf) REFERENCES dbo.servidores(rgf);')
        self.sqldb.commit()

    def insertManyInTB(self, listaDeTuplas, sqlComando):
        self.sqlCursor.executemany(sqlComando, listaDeTuplas)
        self.sqldb.commit()