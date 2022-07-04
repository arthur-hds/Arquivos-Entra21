nome = str(input('Digite seu nome: ')).strip().capitalize()
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
med = (n1+n2+n3+n4) / 4
if med == 10:
    print(f'{nome}, você foi SUPERAPROVADO!!!')
elif med >= 9:
    print(f'{nome}, você não merece palmas, merece tocantis inteiro')
elif med >= 7:
    print(f'{nome}, você foi aprovado')
elif med >= 5:
    print(f'{nome}, você ficou em exame')
elif med >= 3:
    print(f'{nome}, Volte duas casas e tente novamente')
else:
    print(f'{nome}, hj não faro')

