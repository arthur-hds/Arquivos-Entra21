mulheres = []
homens = []
for i in range(1,3):
    for j in range(1, 4):
        if i == 1:
            mulheres.append(input(f'Mulher {j}: ').strip())
        else:
            homens.append(input(f'Homem {j}: ').strip())
    if i == 1:
        print(f'\nMulheres: {mulheres}\n')
    else:
        print(f'\nHomens: {homens}\n')
for k in range(0, 3):
    print(f'Dupla: {mulheres[k]} e {homens[k]}')