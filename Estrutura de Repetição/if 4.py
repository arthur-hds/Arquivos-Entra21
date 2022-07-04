print("-"*50)
print("CASA DE CÂMBIO".center(50))
print("-"*50)
moedas = [4.82, 1, 5.17, 6.04]
tipo_moedas = ['Dólares', 'Reais', 'Euros', 'Libras Esterlinas']
entrada = int(input("""
(1)Dólar
(2)Real
(3)Euro
(4)Libra esterlina
TENHO: """))
saida = int(input("""
(1)Dólar
(2)Real
(3)Euro
(4)Libra esterlina
QUERO: """))
valor_necessario = float(input(f'Quantos {tipo_moedas[saida-1]} você deseja: '))
conv = valor_necessario *(moedas[saida -1] / moedas[entrada -1])
print(f'Voce irá precisar de {round(conv,2)} {tipo_moedas[entrada-1]}')
