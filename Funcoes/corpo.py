import minhasfuncoes

#Ex 1
# print(minhasfuncoes.tri(int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: '))) )

# #Ex 2
# palavra = input('Digite um nome: ').strip()
# l = input('Digite a letra procurada: ').strip()
# print(minhasfuncoes.contar(palavra, l))

#Ex 3
# print(minhasfuncoes.revert(input('Digite um número: ')))

#Ex 4
# print(minhasfuncoes.qnt(input('Digite um número inteiro: ')))

#Ex 5

ehpedra = False
ehpedra2 = False

# minhasfuncoes.exibir_jogadas()

while True:
    jog = int(input('Digite sua jogada'))
    if ehpedra:
        if 2 <= jog <= 3:
            break
    else:
        if 1 <= jog <= 3:
            break

print(f'Você jogou {minhasfuncoes.jogada(jog)}')
