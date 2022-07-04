nome = input('Digite o seu nome: ')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))
med = (n1+n2+n3+n4) / 4
if med >= 7:
    print(f'{nome} - {med}, você foi Aprovado')
elif med >=5:
    print(f'{nome} - {med}, você ficou em exame')
else:
    print(f'{nome} - {med}, po man tu teve o ano todo porra')
