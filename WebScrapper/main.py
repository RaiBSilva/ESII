import sitePMC
import funcoesBD


objDB = funcoesBD.dataBase("DSN=abc;Server=localhost\sqlexpress;Database=Se_Liga_Mogi;Trusted_connection=yes;")

objMogi = sitePMC.siteMogi('http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2')
text = objMogi.getTexto()

rgfServidores = objMogi.extraiRGF(text)
servidoresPublicos = []
remuneracaoServidores = []
descontosServidores = []

for rgf in rgfServidores:
    link = 'http://www.licitacao.pmmc.com.br/Transparencia/detalhamento?rgf=' + rgf
    tentativasDeAcesso = 0
    while tentativasDeAcesso <= 15:
        try:
            objMogi = sitePMC.siteMogi(link)
            text = objMogi.getTexto()
            servidoresPublicos.append(objMogi.extraiDetalhamento(text, rgf))
            remuneracaoServidores.append(objMogi.extraiRendimentos(rgf))
            try:
                descontosServidores.append(objMogi.extraiDescontos(rgf))
            except:
                pass
        except:
            print('Acessando novamente ' + link)
            tentativasDeAcesso = tentativasDeAcesso + 1
        else:
            break

#limpa o banco para a atualização dos dados
objDB.execTruncateTables()

#organização das listas de tuplas
remuneracaoServidores = objMogi.organizaLista(remuneracaoServidores)
descontosServidores = objMogi.organizaLista(descontosServidores)

#inserção dos dados no banco
objDB.insertManyInTB(servidoresPublicos, 'INSERT INTO servidores(rgf, nome_servidor, cargo_servidor, salario_servidor,salario_liquido_servidor,descontos_servidor) VALUES (?, ?, ?, ?, ?, ?);')
objDB.insertManyInTB(remuneracaoServidores, 'INSERT INTO remuneracao_servidores(rgf, nome_remuneracao, valor_remuneracao) VALUES (?, ?, ?);')
objDB.insertManyInTB(descontosServidores, 'INSERT INTO descontos_servidores(rgf, nome_desconto, valor_desconto) VALUES (?, ?, ?);')

