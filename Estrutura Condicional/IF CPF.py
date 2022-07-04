cpf = input('Digite seu CPF: ')
estado = cpf[10]
if len(cpf) != 14:
    print('Digitação errada!')
else:
    print(estado)
    if estado == '0':
        print('Rio Grande do Sul')
    elif estado == '1':
        print('Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins')
    elif estado == '2':
        print('Amazonas, Pará, Roraima, Amapá, Acre e Rondônia')
    elif estado == '3':
        print('Ceará, Maranhão e Piauí')
    elif estado == '4':
        print('Paraíba, Pernambuco, Alagoas e Rio Grande do Norte')
    elif estado == '5':
        print('Bahia e Sergipe')
    elif estado == '6':
        print('Minas Gerais')
    elif estado == '7':
        print('Rio de Janeiro e Espírito Santo')
    elif estado == '8':
        print('São Paulo')
    else:
        print('Paraná e Santa Catarina')
