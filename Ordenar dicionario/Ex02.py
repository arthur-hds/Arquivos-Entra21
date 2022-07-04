from random import randint
from operator import itemgetter
dic = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6)
}
dicNovo = sorted(dic.items(), key=itemgetter(1),reverse=True)
dic.clear()
for i,j in dicNovo:
    dic[i] = j
    print(f'{i} - {j}')

