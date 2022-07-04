contRepetidoRemovidos = contDup = contUnico = 0
arqAntigo = open('clientes sistema antigo.txt', 'r')
arqNova = open('clientes sistema novo.txt', 'r')
novaLista = arqNova.read().splitlines()
antigaLista = arqAntigo.read().splitlines()
juncao = []
juncao.extend(novaLista), juncao.extend(antigaLista)
for i in set(juncao):
    if juncao.count(i) > 1:
        contDup += 1
        contRepetidoRemovidos += juncao.count(i) - 1
    else:
        contUnico += 1
print(f'Cadastros Duplicados : {contDup}')
print(f'Cadastros Únicos : {(len(novaLista) + len(antigaLista)) - contRepetidoRemovidos}')
print(f'Cadastros nas duas listas : {len(antigaLista) + len(novaLista)}')
print(f'Cadastros lista antiga : {len(antigaLista)}')
print(f'Cadastros lista nova : {len(novaLista)}')
print(f'Repetidos removidos : {contRepetidoRemovidos}')
print(f'Itens a remover para não ter duplicados : {contRepetidoRemovidos - contUnico}')
