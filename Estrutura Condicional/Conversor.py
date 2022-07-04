print('-'*30)
print('Selecione uma opção'.center(30))
print('-'*30)
print('''1 - Converter de Celsius para Kelvin
2 - Converter de Celsius para Fahrenheit
3 - Converter de Kelvin para Celsius
4 - Converter de Kelvin para Fahrenheit
5 - Converter de Fahrenheit para Celsius
6 - Converter de Fahrenheit para Kelvin
-----------------------------------------------''')
opc = int(input('Digite a sua opção: '))
print('-'*30)
if opc <= 2:
    v1 = float(input('Valor Celsius: '))
    if opc == 1:
        print(f'{v1 + 273:.2f}Kelvin')
    else:
        print(f'{v1*1.8+32:.2f} Fahrenheit')
elif opc <= 4:
    v1 = float(input('Valor Kelvin: '))
    if opc == 3:
        print(f'{v1 - 273:.2f} Celsius')
    else:
        print(f'{(v1-273)*1.8+32:.2f} Fahrenheit')
elif opc <= 6:
    v1 = float(input('Valor Fahrenheit: '))
    if opc == 5:
        print(f'{(v1-32)/1.8:.2f} Celsius')
    else:
        print(f'{(v1-32) *(5/9)+273:.2f} Kelvin')
