from random import randint, choice
cartao = ''
soma = cont = bandeira = numRes = 0
#5486 6666 4945 6811
numBandVal = []
elo = ['636368', '438935', '504175', '451416', '636297', '506699', '5067', '4576', '4011']
masterCard = ['51', '52', '53', '54', '55']
aura = ['50']
visa = ['4']
americanExpress = ['34', '37']
dinersclub = ['36', '38', '30']
opc = int(input('Digite sua opção:\n1)Gerar Cartão\n2)Validar Cartão\n'))


while cartao == '':
    bandeira = int(input('''Digite a sua opção de bandeira:
[1] Visa ;
[2] MasterCard ;
[3] Aura ;
[4] Elo ; 
[5] AmericanExpress ;
[6] Diner's Club
'''))
    if bandeira == 1:
        cartao += visa[0]
        DigNecessarios = 15
        numBandVal = visa
    elif bandeira == 2:
        cartao += choice(masterCard)
        DigNecessarios = 15
        numBandVal = masterCard
    elif bandeira == 3:
        cartao += choice(aura)
        DigNecessarios = 15
        numBandVal = aura
    elif bandeira == 4:
        cartao += choice(elo)
        DigNecessarios = 15
        numBandVal = elo
    elif bandeira == 5:
        cartao += choice(americanExpress)
        DigNecessarios = 14
        numBandVal = americanExpress
    elif bandeira == 6:
        cartao += choice(dinersclub)
        DigNecessarios = 13
        numBandVal = dinersclub
    else:
        print('Cartão não selecionado')
    cont = len(cartao)


if opc == 1:
    while cont < DigNecessarios:
        rand = randint(0, 9)
        cartao += str(rand)
        cont += 1
else:
    if opc == 2 and bandeira != 4:
        cartao = cartao[0]
    else:
        cartao = ''
    cartao += input(f"Digite o cartão de crédito: \033[32m{cartao}\033[m").strip().replace(' ', '').replace(' ', '').replace(' ', '')


if bandeira == 5: numRes = 1
cont = 0
while cont < DigNecessarios:
    if cont % 2 == numRes:
        cartaoINT = int(cartao[cont])
        if cartaoINT >= 5:
            cartaoINT = (cartaoINT * 2) - 9
        else:
            cartaoINT *= 2
    else:
        cartaoINT = int(cartao[cont])
    soma += cartaoINT
    cont += 1
soma %= 10
soma -= 10
soma = str(soma)

if cartao[len(cartao)-1] == soma[len(soma)-1] and opc == 2 and (cartao[:len(numBandVal[0])] in numBandVal or cartao[:len(numBandVal[6])] in numBandVal):

    print(30*'-')
    print('Seu cartão é válido.'.center(30))
    print(30 * '-')
elif opc == 1:
    cartao += soma[1]
    print(30 * '-')
    print('Seu cartão é válido.'.center(30))
    print(30 * '-')
else:
    print(30 * '-')
    print('Seu cartão é inválido.'.center(30))
    print(30 * '-')

if len(cartao) == 16:
    print(f'CARTÃO: {cartao[:4]} {cartao[4:8]} {cartao[8:12]} {cartao[12:]}')
else:
    print(f'CARTÃO: {cartao[:4]} {cartao[4:10]} {cartao[10:]}')