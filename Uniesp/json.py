#teste JSON
from __future__ import print_function
import json

dicionario = {}
dicionario['Nome'] = input('Nome do cliente: ')
dicionario['Divida'] = input('Valor da Divida: ')
dicionario['Telefone'] = input('Telefone do Cliente: ')
dicionario['Endereço'] = input('Endereço do Cliente: ')

open('dicionario.json','w').write(json.dumps(dicionario))

with open('dicionario.json', 'r') as file_json:
    dicionario_2 = json.loads(file_json.read())

print(dicionario_2)