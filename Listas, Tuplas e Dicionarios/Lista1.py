num = []
nsoma = 0
while True:
    num.append(int(input('Digite seu número: ')))
    print('-'*30)
    print(f'Números digitados até o momento \033[1m{num}\033[m')
    res = str(input('Deseja continuar? [S/N]')).strip().upper()
    if res == 'N': break
num.sort()
print(f'Números em ordem crescente : {num}')
num.sort(reverse=True)
print(f'Números em ordem decrescente : {num}')
for i in num:
    nsoma += i
print(f'Soma de todos os números : {nsoma}')
print(f'Média de todos os números : {nsoma/len(num)}')
