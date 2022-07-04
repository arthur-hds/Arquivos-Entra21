from random import randint
dic = {'nome': input('Digite seu nome: '),
    'idade': 2022 - int(input('Digita seu ano de nascimento')),
    "CTPS": input('Digite seu número de carteira de trabalho: ').strip()}
if dic['CTPS'] != '0':
    dic["Ano"] = 2022
    dic["Salário"] = randint(1212, 4800)
    dic["Aposentadoria"] = 2022 + (randint(25,50) + 50)
for i,j in dic.items():
    print(f'{i} -- {j}')