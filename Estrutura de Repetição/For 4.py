res = ''
while res != 'S' and res != 'N':
    res = input('Deseja ver uma tabuada? [S ou N]\nReposta: ').upper().strip()
while res == 'S':
    n = int(input('\nTabuada de: '))
    print()
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n*i}')
    res = ''
    while res != 'S' and res != 'N':
        res = input('Deseja ver uma tabuada? [S ou N] ').upper().strip()
