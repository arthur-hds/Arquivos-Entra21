produtos = []
preco = []
qnt = int(input('Quantos produtos você deseja cadastrar?\nResposta:  '))
print('='*30)
for i in range(0, qnt):
    produtos.append(input(f'\nProduto {i+1}: ').strip().capitalize())
    preco.append(input(f'Preço: R$ ').strip())
print('='*30, end='')
for j in range(0, qnt):
    print(f'\nProduto: {produtos[j]} - Preço: R$ {preco[j]}')