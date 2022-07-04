# chave = '1318101792142700012565001000000030988725117'
# mult = 2
# posiçao = 43
# chaveINT = 0
# chaveINT = list()
#
# while mult > 1:
#     chaveINT += int(chave[posiçao])*mult
#     posiçao -= 1
#     mult += 1
# print(chaveINT)


cont = 43
mult = 2
nota = list('43171207364617000135550000000120141000120146')
print(nota)

while cont > 0:
    print(f'{cont} - {mult} x {nota[cont-1]}')
    mult += 1
    if mult == 10:
        mult = 2
    cont -= 1
























# if len(chave) != 44 or not chave.isnumeric():
#     print('CV Inválido,revise os dados inseridos')
#
# else:
#     if (chave == '0'*44 or chave == '1'*44 or chave == '2'*44 or chave == '3'*44 or chave == '4'*44
#          or chave == '5'*44 or chave == '6'*44 or chave == '7'*44 or chave == '8'*44 or chave == '9'*44):
#         print(f'CPF digitado foi: {chave[:2]}-{chave[2:6]}-{chave[6:20]}-{chave[20:22]}-{chave[22:25]}-{chave[25:34]}-{chave[34:35]}-{chave[35:43]}-{chave[43:]}\nCV INVÁLIDO')
#
# # mult = [9, 8, 7, 6, 5, 4, 3, 2]
# # mult += 1
# # cont = 43
# cont -= 1


#
#     div = mult % 11
#     div_novo = 11 - {div}
