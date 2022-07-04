from Funcoes import situacao
dic = {}
nome = input('Digite o nome: ').strip().capitalize()
media = float(input('Digite sua média: '))
for i, j in situacao(nome, media).items():
    print(f'{i} - {j}')