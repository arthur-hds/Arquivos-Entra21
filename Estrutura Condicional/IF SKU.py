print('''Tipos de Produto:
1- MON - Monitor
2- TEC - Teclado
3- MOU - Mouse''')
tp = input('Digite o seu pedido: ').upper()
if tp == '1' or tp == 'MON':
    tpP = 'MON Monitor'
elif tp == '2' or tp == 'TEC':
    tpP = 'TEC Teclado'
elif tp == '3' or tp == 'MOU':
    tpP = 'MOU Mouse'
print('''Cor:
1- PR - Preto
2- AZ - Azul
3- VM - Vermelho
4- BR - Branco''')
cor = input('Digite o seu pedido: ').upper()
if cor == '1' or cor == 'PR':
    corP = 'PR Preto'
elif cor == '2' or cor == 'AZ':
    corP = 'AZ Azul'
elif cor == '3' or cor == 'VM':
    corP = 'VM Vermelho'
elif cor == '4' or cor == 'BR':
    corP = 'BR Branco'
print('''Material de Fabricação:
1- PP = Polipropileno
2- PE = Polietileno
3- PO = Poliamida''')
mf = input('Digite o seu pedido: ').upper()
if mf == '1' or mf == 'PP':
    mfP = 'PP Polipropileno'
elif mf == '2' or mf == 'PE':
    mfP = 'PE Polietileno'
elif mf == '3' or mf == 'PO':
    mfP = 'PO Poliamida'
print('''Geração:
1- 1G - 1ª Geração
2- 2G - 2ª Geração
3- 3G - 3ª Geração''')
ger = input('Digite o seu pedido: ').upper()
if ger == '1' or ger == '1G':
    gerP = '1G 1 Geração'
elif ger == '2' or ger == '2G':
    gerP = '2G 2 Geração'
elif ger == '3' or ger == '3G':
    gerP = '3G 3 Geração'
ano = int(input('Digite o ano de fabricação: '))
if '123 MON MOU TEC' in tp and '1234 PR AZ VM BR' in cor and '123PPPEPO' in mf and '1231G2G3G' and 1990 > ano > 2022:
    print('bixo confere as informações ai')
else:
    print(f'{tpP[3:]} {corP[2:]} {mfP[2:]} {gerP[2:]} {ano} = {tpP[0:3]}-{corP[0:2]}-{mfP[0:2]}-{gerP[0:2]}/{ano}')
