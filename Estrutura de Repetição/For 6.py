from random import randint
arquivo = open('listatimes.txt', 'r')
times = arquivo.read().splitlines()
# times = ['Vasco', 'Flamengo', 'Corinthians', 'Palmeiras', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba',
#          'Avaí', 'América-MG', 'Bragantino', 'Internacional', 'Fluminense', 'Goiás', 'Cuiabá', 'Athletico-PR',
#          'Juventude', 'Ceará', 'Atlético Goianiense']
pont = [0] * len(times)
gols = [0] * len(times)
for i in times:
    print(f'\nJogos do {i}: \n\n')
    for j in range(0, len(times)):
        if times[j] != i:
            gol1 = randint(0, 6)
            gol2 = randint(0, 6)
            print(f'{i} [{gol1}] X [{gol2}] {times[j]}')
            if gol1 > gol2:
                pont[times.index(i)] += 3
            elif gol1 < gol2:
                pont[j] += 3
            else:
                pont[times.index(i)] += 1
                pont[j] += 1
            gols[times.index(i)] += gol1
            gols[j] += gol2
if pont.count(max(pont)) > 1:
    print(f'\nTime campeão : {times[gols.index(max(gols))]} | Pontuação : {pont[gols.index(max(gols))]} | Gols:  {max(gols)}')
else:
    print(f'\nTime campeão : {times[pont.index(max(pont))]} | Pontuação : {max(pont)} | Gols:  {gols[times.index(times[pont.index(max(pont))])]}')