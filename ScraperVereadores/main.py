import Pdf02_2020
import funcoesBD

objDB = funcoesBD.dataBase("DSN=SQLEXPRESS;Server=localhost\sqlexpress;Database=Se_Liga_Mogi;Trusted_connection=yes;")

funcionarios02_2020 = Pdf02_2020.LerPdf02()
funcionario_refatorados = []
for i in funcionarios02_2020:
    funcionario_refatorados.append((i[0],i[1],i[2],0))

objDB.insertManyInTB(funcionario_refatorados,'INSERT INTO parlamentares(id_parlamentar, nome_parlamentar, cargo_parlamentar, total_faltas) VALUES (?, ?, ?, ?);')
