# usu = 'ART'
# senha = '09012006'
# while True:
#     loginUsu = input('Usuário: ').upper().strip()
#     loginSen = input('Senha: ').upper().strip()
#     if loginSen == senha and loginUsu == usu:
#         break
#     else:
#         print('Usuário ou senha digitados errados, tente novamente!')
# print('Login realizado')

# nome = input('Informe seu nome: ').strip().capitalize()
# if len(nome) > 8:
#     print(f"o nome '{nome}' é muito grande!")
# elif len(nome) > 6:
#     print(f"o nome '{nome}' é grande!")
# else:
#     print(f"o nome '{nome}' é pequeno")
#
# horario = input('Digite sua disponibilidade de horário: ').strip().replace(' ', ':')
# hora = int(horario[:2])
# minuto = int(horario[3:])
# if 12 >= hora >= 5 or (hora == 13 and minuto <= 30):
#     print('Turno 1 - 05:00 - 13:30 ')
# elif 20 >= hora >= 13 or (hora == 21 and minuto <= 59):
#     print('Turno 2 - 13:31 - 21:59 ')
# else:
#     print('Turno 3 - 22:00 - 04:59 ')

# meu_nasc = input('Digite sua data de nascimento [XX/XX/XXXX]: ').strip().replace('/', '')
# data = input('Digite outra data de nascimento [XX/XX/XXXX]: ').strip().replace('/', '')
# if int(meu_nasc[4:]) < int(data[4:]):
#     print(f'Você é {(int(meu_nasc[4:]) - int(data[4:]))* -1} ano(s) mais velho')
# elif int(meu_nasc[4:]) > int(data[4:]):
#     print(f'Você é {(int(meu_nasc[4:]) - int(data[4:]))} ano(s) mais novo')
# elif int(meu_nasc[2:4]) < int(data[2:4]):
#     print(f'Você é {(int(meu_nasc[2:4]) - int(data[2:4]))* -1} mes(es) mais velho')
# elif int(meu_nasc[2:4]) > int(data[2:4]):
#     print(f'Você é {(int(meu_nasc[2:4]) - int(data[2:4]))} mes(es) mais novo')
# elif int(meu_nasc[:2]) < int(data[:2]):
#     print(f'Você é {(int(meu_nasc[:2]) - int(data[:2])) *-1} dia(s) mais velho')
# elif int(meu_nasc[:2]) > int(data[:2]):
#     print(f'Você é {(int(meu_nasc[:2]) - int(data[:2]))} dia(s) mais novo')
# else:
#     print(f'Vocês dois nasceram no mesmo dia!')

# notas = 0
# freq = int(input('Informe sua frequência: '))
#
# for c in range(3):
#         n = float(input(f'Digite sua {c + 1} nota: '))
#         while n >10 or n<0:
#             n = float(input(f'Digite novamente sua {c + 1} nota: '))
#         notas += n
# print(f'Sua frequência é de {freq}%')
# print(f'Sua média é de {notas/3:.2f}')
# if freq < 75 or notas/3 < 7:
#     print('Reprovado!')
# else:
#     print('Aprovado!')


# n1 = 1
# n2 =0
# num = int(input('Digite a quantidade de termos: '))
# for i in range(num):
#     print(f'{n1}',end='')
#     if i < num-1: print(',',end='')
#     nRes = n1
#     n1 += n2
#     n2 = nRes


# lista = [1, 3, 5]
# novo = 2
# lista.insert(1, novo)
# print(lista)

# letra = ['A barata diz que tem',
#          'sete saias de filó,',
#          'é mentira da barata',
#          'ela tem é uma só',
#          'hahaha, hohoho',
#          'ela tem é uma só']
# for i in letra:
#     print(i)

# arthur = []
# for i in range(3):
#     arthur.append(input('Digite um nome: ').strip().capitalize())
# print(arthur)

# COPIA NAO COMEDIA
