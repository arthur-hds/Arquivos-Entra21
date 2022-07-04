from random import randint, choice

print("Selecione uma opção:\n1 - Gerar Cartão\n2 - Validar Cartão")
opcao = int(input("Opção: "))
if opcao == 1:
    valido = False
    nomeBandeira = ""
    opcaowhile = 0
    while opcaowhile < 1 or opcaowhile > 8:
        elo = ['636368', '438935', '504175', '451416', '636297', '506699', '5067', '4576', '4011']
        masterCard = ['51', '52', '53', '54', '55']
        discover = ['6011', '65', '62', '64']
        aura = ['50']
        visa = ['4']
        americanExpress = ['34', '37']
        dinersclub = ['36', '38', '39', '300', '301', '302', '303', '304', '305']
        cartao = ""
        mensagem = """Selecione a opcao:
        1 - ELO
        2 - DISCOVER
        3 - MASTERCARD
        4 - AURA
        5 - VISA
        6 - AMERICAN EXPRESS
        7 - DINER'S CLUB
        8 - DESISTIR
        """
        print(mensagem)
        opcaowhile = int(input("Opção: "))
        if opcaowhile == 1:
            cartao += choice(elo)
            digitos = 16 - len(cartao)
            nomeBandeira = "ELO"
        elif opcaowhile == 2:
            cartao += choice(discover)
            digitos = 16 - len(cartao)
            nomeBandeira = "DISCOVER"
        elif opcaowhile == 3:
            cartao += choice(masterCard)
            digitos = 16 - len(cartao)
            nomeBandeira = "MASTERCARD"
        elif opcaowhile == 4:
            cartao += choice(aura)
            digitos = 16 - len(cartao)
            nomeBandeira = "AURA"
        elif opcaowhile == 5:
            cartao += visa[0]
            digitos = 15
            nomeBandeira = "VISA"
        elif opcaowhile == 6:
            cartao += choice(americanExpress)
            digitos = 15 - len(cartao)
            nomeBandeira = "AMERICAN EXPRESS"
        elif opcaowhile == 7:
            cartao += choice(dinersclub)
            digitos = 16 - len(cartao)
            nomeBandeira = "DINER'S CLUB"
        elif opcaowhile == 8:
            break

        if opcaowhile < 1 or opcaowhile > 8:
            print("Opção inválida. Digite novamente")
        else:
            cont = soma = 0
            while not valido:
                while cont < digitos:
                    num = randint(0, 9)
                    cartao += str(num)
                    cont += 1

                cont = 0

                while cont < len(cartao):
                    num = int(cartao[cont])

                    if cont % 2 == 0:
                        num *= 2
                        if num > 9:
                            num -= 9

                    soma += num

                    cont += 1

                resto = soma % 10

                if resto == 0:
                    valido = True
                    print(f"Seu cartão foi gerado.\nDados:\nBandeira: {nomeBandeira}\nNumero: {cartao}")

elif opcao == 2:
    cont = soma = 0
    nomeopcao = "Não reconhecida"
    nomeBandeira = ""

    cartao = input("Cartao: ").replace(" ", "")

    if len(cartao) < 12 or len(cartao) > 16:
        print(f"Cartão não é valido. Não existe cartão com {len(cartao)} digitos")
    else:
        while cont < len(cartao):
            num = int(cartao[cont])

            if cont % 2 == 0:
                num *= 2
                if num > 9:
                    num -= 9

            soma += num

            cont += 1

        resto = soma % 10

    if cartao[0:6] == "636368" or cartao[0:6] == "438935" or cartao[0:6] == "504175" or cartao[0:6] == "451416" or cartao[0:6] == "636297" or cartao[0:4] == "5067" or cartao[0:4] == "24576" or cartao[0:4] == "4011" or cartao[0:6] == "506699":
        nomeBandeira = "ELO"
    elif cartao[0:4] == "6011" or cartao[0:2] == "65" or cartao[0:2] == "62":
        nomeBandeira = "DISCOVER"
    elif cartao[0:2] == "51" or cartao[0:2] == "52" or cartao[0:2] == "53" or cartao[0:2] == "54" or cartao[
                                                                                                     0:2] == "55":
        nomeBandeira = "MASTERCARD"
    elif cartao[0:1] == "50":
        nomeBandeira = "AURA"
    elif cartao[0] == "4":
        nomeBandeira = "VISA"
    elif cartao[0:1] == "34" or cartao[0:1] == "37":
        nomeBandeira = "AMERICAN EXPRESS"
    elif cartao[0:1] == "36" or cartao[0:1] == "38":
        nomeBandeira = "DINER'S CLUB"
    elif cartao[0] == "0":
        nomeBandeira = "ISO/TC e outras atribuições da industria."
    elif cartao[0] == "1":
        nomeBandeira = "Companhias aéreas."
    elif cartao[0] == "2":
        nomeBandeira = "Campanhas aéreas, financeiras."
    elif cartao[0] == "3":
        nomeBandeira = "Viagens e entretenimento."
    elif cartao[0] == "6":
        nomeBandeira = "Merchandising e bancário/financeiro."
    elif cartao[0] == "7":
        nomeBandeira = "Petróleo e atribuições futuras da indústria."
    elif cartao[0] == "8":
        nomeBandeira = "Saúde, telecomunicação e atribuições futuras da indústria."
    elif cartao[0] == "9":
        nomeBandeira = "Atribuições por organismo nacionais de normalização."

    if resto == 0:
        print(f"Cartão válido. Sua opcao é: {nomeBandeira}.")
    else:
        print("Cartão inválido.")