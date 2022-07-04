val = []
contBool = contFl = contInt = contStr = 0
for i in range(0, 3):
    val.append(input('Digite alguma coisa: ').capitalize())
    try:
        val[i] = int(val[i])
        contInt += 1
    except:
        try:
            val[i] = float(val[i])
            contFl += 1
        except:
            try:
                if val[i] == 'True' or val[i] == 'False':
                    val[i] = bool(val[i])
                    contBool += 1
                else:
                    contStr += 1
            except:
                print('Deu errado')
                
val.reverse()
print(f'A lista ao contrário é {val}')
print(f'''Quantidade de INT : {contInt}
Quantidade de STR: {contStr}
Quantidade de FLOAT: {contFl}
Quantidade de BOOL: {contBool}''')
