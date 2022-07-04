# arq = open('nomes.txt', 'r')
# listas = arq.read().splitlines()
# listas.sort()
# for i in range(0, len(listas)):
#     print(f'{listas[i]} - {i+1}')
dic = {
    "Jonas": "jonareiters@hotmail.com",
    "susan": "susan.reiter@hotmail.com",
    "Professora" : "contato@reiter.page" }
print(dic["susan"])
print(dic.get("Claudia", "Nao tem"))
dic['Arthur'] = dic['Jonas']
dic['Arthur'] += 'a'
print(dic)

dic["Jonas"] = dic["Arthur"]
del dic["Arthur"]
print(dic)
if "Jonas" in dic.keys():
    print('God')
dic.pop('Jonas')
print(dic)
dic.popitem()
print(dic)
# print(dic.keys())
# print(dic.values())
# for i in dic:
#     print(i)
# for i, v in dic.items():
#     print(i, v)

chave = ['A', 'B', 'C']
valor = 0
novo_dic = dict.fromkeys(chave, valor)
print(novo_dic)

lista1 = ['Pele', 'Maradona', 'Ronaldo']
gols = [100, 89, 76]
dic3 = {}
for i in range(len(lista1)):
    dic3[lista1[i]] = gols[i]
print(dic3)

dic = {**dic, **dic3}
print(dic)

dic.clear()
print(dic)