OP = 25
ON = 12
ABP = 12
ABN = 27
BP = 30
BN = 4
AN = 22
AP = 23
bolsas = OP + ON + ABP + ABN + BP + BN + AN + AP
print(bolsas)
id = int(input('Digite sua idade: '))
if 18 < id <= 65:
    opc = input('Deseja DOAR ou RETIRAR sangue: ').upper()
    if opc == 'RETIRAR' or opc == 'DOAR':
        qnt = int(input(f'O quanto você deseja {opc}: '))
        if 'RETIRAR' in opc:
            qnt *= -5
            print(qnt)
        tip = input('''Digite seu tipo sanguíneo:
         [O+] | [O-]
         [A+] | [A-]
         [B+] | [B-]
         [AB+] | [AB-]
         ''').strip().upper()
        if tip == 'O+':
            if qnt < OP and :
                OP += qnt
                print('Operação realizada com sucesso!')
            else:
                print(f'Você está tentando tirar {qnt*-1} bolsas de sangue O+ com apenas {OP} bolsas ')
        elif tip == 'O-':
            if qnt < ON:
                ON += qnt
                print('Operação realizada com sucesso!')
            else:
                print(f'Você está tentando tirar {qnt*-1} bolsas de sangue O- com apenas {ON} bolsas ')
        elif tip == 'A+':
            if qnt < AP:
                AP += qnt
                print('Operação realizada com sucesso!')
            else:
                print(f'Você está tentando tirar {qnt * -1} bolsas de sangue A+ com apenas {AP} bolsas ')
        elif tip == 'A-':
            if qnt < AN and opc == 'RETIRAR':
                AN += qnt
                print('Operação realizada com sucesso!')
            elif opc == 'DOAR':
                AN += qnt
            else:
                print(f'Você está tentando tirar {qnt*-1} bolsas de sangue A- com apenas {AN} bolsas ')
        elif tip == 'AB+':
            if qnt < ABP and opc == 'RETIRAR':
                ABP += qnt
                print('Operação realizada com sucesso!')
            elif opc == 'DOAR':
                ABP += qnt
            else:
                print(f'Você está tentando tirar {qnt * -1} bolsas de sangue AB+ com apenas {ABP} bolsas ')
        elif tip == 'AB-':
            if qnt < ABN and opc == 'RETIRAR':
                ABN += qnt
                print('Operação realizada com sucesso!')
            elif opc == 'DOAR':
                ABN += qnt
                print('Operação realizada com sucesso!')
            else:
                print(f'Você está tentando tirar {qnt * -1} bolsas de sangue AB- com apenas {ABN} bolsas ')
        else:
            print('Padrão incorreto!')
        print()