continuar = 's'
cont = 1
while continuar == 's':
    print(cont)
    cont += 1
    continuar = input('Deseja continuar?: ').strip().lower()
print('Cabo')