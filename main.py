import requests
import urllib.request
import json

res = urllib.request.urlopen('http://www.licitacao.pmmc.com.br/Transparencia/vencimentos2')
res_body = res.read()

print(res_body)