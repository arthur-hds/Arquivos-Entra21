lista1 = list(range(5,11))
lista2 = [3, 5, 5, 7, 9, 3]

set1 = set(lista1)
set2 = set(lista2)
print(set2)
print(lista2)

if len(lista2) == len(set2):
    print('Sem duplicadas')
else:
    print('Duplicadas')

print(f'Set 2 {set2}')
set3 = {4, 5, 6, 7, 9}
set3.update('1')
print(f'Union {set2.union(set3)}')
print(f'Set 3{set3}')
print(f'Set 2{set2}')

print(f'Interseção {set2.intersection(set3)}')
print(f'Diferença Simétrica (O que não está na interseção) {set2.symmetric_difference(set3)}')
print(f'Diferença (Só tem no set2 e não no set3) {set2.difference(set3)}')

if 9 in set2.intersection(set3):
    print('Tem')

set2.add(1)
print(set2)

tupla1 = (3, 5, 13, 290)
lista3 = [260, 220, 240]

# set2.add(tupla1) #Coloca lista com colchetes MANEIRA ERRADA
# print(set2)

set2.update(tupla1) #Coloca lista sem colchetes, só valores MANEIRA CERTA
print(set2)

set2.update(lista3)
print(set2)

set2.remove(220) #Se numero nao existir, programa da erro
print(set2)

set2.discard(230) #Se numero nao existir, nada acontece
print(set2)

set2.pop()
print(set2)

set4 = set(range(1, 10))
print(set4)

set4.clear() #Apaga conteudo e Type continua como Set
print(set4)

# set4 = {} #Renova todos os itens mas Type é tido como DICIONÁRIO
# print(set4)

for i in set2:
    print(i)