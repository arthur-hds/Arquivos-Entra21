arqCandidatoA = open('Candidato A.txt', 'r')
arqCandidatoB = open('Candidato B.txt', 'r')
listaA = arqCandidatoA.read().splitlines()
listaB = arqCandidatoB.read().splitlines()
print(f'Candidato A {len(listaA)}')
print(f'Candidato B {len(listaB)}')
if len(listaA) == len(listaB):
    print('Deu empate')
elif len(listaA) > len(listaB):
    print('Candidato A ganhou')
else:
    print('Candidato B ganhou')
print(f'Pessoas que votaram nos 2 candidatos: {len(set(listaA).intersection(listaB))}')
print(f'Pessoas que não votaram: {(len(set(listaA)) + len(set(listaB))) - 27}')
print(len(set(listaB)))
