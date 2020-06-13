
def maiorquetres(num):
    numinteiro = int(num[:4])
    if num[4] == "9":
        numinteiro = numinteiro + 1
    num = str(numinteiro)
    num = num + '.0'
    return num


def tresNumeros(num):
    num = num + '.0'
    return num

def pertenceaosmilhares(num, quant):
    for i in range(0, 4-quant):
        num = num + '0'
    num = num + '.0'
    return num

def transformaInteiro(numero):
    strNum = str(numero)
    aux = 0
    if strNum[1] == '.':
        strNum = strNum.replace('.','')
        aux = 1
    if strNum.isnumeric():
        if len(strNum) > 4:
            strNum = maiorquetres(strNum)
        elif len(strNum) <= 3 and aux != 1:
            strNum = tresNumeros(strNum)
        elif len(strNum) <= 3 and aux == 1:
            strNum = pertenceaosmilhares(strNum, len(strNum))
    return strNum
