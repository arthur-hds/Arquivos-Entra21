par = impar = bissexto = futuro = passado = 0
while True:
    ano = int(input('Digite um ano: [0 para parar] '))
    if ano == 0:
        break
    anoS = str(ano)

    if anoS[2:] == '00':
        if ano % 400 == 0:
            bissexto += 1
    else:
        if ano % 4 == 0:
            bissexto += 1
    if ano % 2 == 0:
        par += 1
    else:
        impar += 1
    if ano > 2022:
        futuro += 1
    else:
        passado += 1
print(f'Anos pares: {par}')
print(f'Anos impares: {impar}')
print(f'Quantidade de anos bissextos: {bissexto}')
print(f'Anos futuros: {futuro}')
print(f'Anos passados: {passado} ')