# import requests
# arq = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# cidades = dict(arq.json())
# while True:
#     escola = input('Digite uma escola').capitalize()
#     for i, j in cidades.items():
#         if i[0] == escola[0]:
#             print(i, j)



# import requests
# arq = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# cidades = dict(arq.json())
# for i, j in cidades.items():
#     if len(i) > 14:
#         print(i, j, '- Nome muito grande')
#     elif len(i) < 8:
#         print(i, j, '- Nome curto')
#     else:
#         print(i, j, '- Nome grande')



# import requests
# arq = requests.get('https://times-5e780-default-rtdb.firebaseio.com/Times.json')
# dicEXE = dict(arq.json())
# dic = {
#     input("Digite seu nome") : input("Digite seu time")
# }
# dic = requests.post('https://times-5e780-default-rtdb.firebaseio.com/Times.json', data=f'"{dic}"')



# import requests
#
# cores = requests.get('https://cores-d86c6-default-rtdb.firebaseio.com/Cores.json')
#
# cor1 = int(input('01-Azul\n02-Amarelo\n04-Vermelho'))
# cor2 = int(input('01-Azul\n02-Amarelo\n04-Vermelho'))
#
# if cor1 == cor2:
#   cor = cor1
# else:
#   cor = cor1+cor2
# print(cores.json()[cor])




import requests
cep = input('Insira o seu CEP:\n')
api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(f'Endereço: {api.json()["logradouro"]}')
print(f'Estado: {api.json()["uf"]}')
print(f'Bairro: {api.json()["bairro"]}')
print(f'Cidade: {api.json()["localidade"]}')
print(f'DDD: {api.json()["ddd"]}')
# 89069040
