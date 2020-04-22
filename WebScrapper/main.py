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
    while True:
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
        else:
            break

remuneracaoServidores = objMogi.organizaLista(remuneracaoServidores)
descontosServidores = objMogi.organizaLista(descontosServidores)
objDB.insertManyInTB(servidoresPublicos, 'INSERT INTO servidores(rgf, nome_servidor, cargo_servidor, salario_servidor,salario_liquido_servidor,descontos_servidor) VALUES (?, ?, ?, ?, ?, ?);')
objDB.insertManyInTB(descontosServidores, 'INSERT INTO remuneracao_servidores(rgf, nome_remuneracao, valor_remuneracao) VALUES (?, ?, ?);')
objDB.insertManyInTB(remuneracaoServidores, 'INSERT INTO descontos_servidores(rgf, nome_desconto, valor_desconto) VALUES (?, ?, ?);')

