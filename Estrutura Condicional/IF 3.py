n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1>=n2:
    if n1>=n3:
        if n3>=n2:
            n1, n2, n3 = n1, n3, n2
elif n2>=n3:
    if n3>=n1:
        n1, n2, n3 = n2, n3, n1
    else:
        n1, n2, n3 = n2, n1, n3
else:
    n1, n2, n3 = n1, n2, n3
print(f'Crescente: {n1:.0f}, {n2:.0f} e {n3:.0f}')
print(f'Decrescente: {n3:.0f}, {n2:.0f} e {n1:.0f}')
