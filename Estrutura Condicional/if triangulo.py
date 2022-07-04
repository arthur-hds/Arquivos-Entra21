m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
if m1 < (m2+m3) and m2 < (m1+m3) and m3 < (m2+m1):
    print('TRIÂNGULO POSSÍVEL', end=': ')
    if m1 == m2 == m3:
        print('EQUILÁTERO')
    elif m1 == m2 or m2 == m3 or m1 == m3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('TRIÂNGULO IMPOSSÍVEL')