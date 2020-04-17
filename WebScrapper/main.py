import sitePMC
import funcoesBD


objDB = funcoesBD.dataBase("DSN=abc;Server=localhost\sqlexpress;Database=Se_Liga_Mogi;Trusted_connection=yes;")

objMogi = sitePMC.siteMogi('http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2')
text = objMogi.getTexto()

rgfServidores = objMogi.extraiRGF(text)
servidoresPublicos = []
remuneracaoServidores = []
descontosServidores = []

for i in range(0, len(rgfServidores)):
    link = 'http://www.licitacao.pmmc.com.br/Transparencia/detalhamento?rgf=' + rgfServidores[i]
    while True:
        try:
            objMogi = sitePMC.siteMogi(link)
            text = objMogi.getTexto()
            servidoresPublicos.append(objMogi.extraiDetalhamento(text,rgfServidores[i]))
            remuneracaoServidores.append(objMogi.extraiRendimentos(rgfServidores[i]))
            try:
                descontosServidores.append(objMogi.extraiDescontos(rgfServidores[i]))
            except:
                pass
        except:
            print('Acessando novamente ' + link)
        else:
            break

remuneracaoServidores = objMogi.organizaLista(remuneracaoServidores)
descontosServidores = objMogi.organizaLista(descontosServidores)
objDB.insertInTBservidores(servidoresPublicos)
objDB.insertInTBdescontos(descontosServidores)
objDB.insertInTBremuneracao(remuneracaoServidores)

