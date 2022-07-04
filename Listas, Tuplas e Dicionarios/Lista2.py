nomes = []
while True:
    nome = str(input('Digite um nome, (PARE) para encerrar:')).strip().upper()
    while nome.isnumeric() is True:
        nome = str(input('Apenas nomes sem números são permitidos: '))
    if nome == 'PARE':
        break
    nomes.append(nome)
nomes.sort()
print(f'Nomes em ordem crescente: {nomes}')
nomes.sort(reverse=True)
print(f'Nomes em ordem decrescente: {nomes}')
print(f'Nomes cadastrados no total: {len(nomes)}')
qtdCarlos = nomes.count('CARLOS')
print(f'Existem {qtdCarlos} Carlos nos nomes informados')