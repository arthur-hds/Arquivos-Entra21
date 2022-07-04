from random import randint

def tri(med1, med2, med3):
    if med1 > med2+med3 or med2 > med1+med3 or med3 > med2+med1:
        return 'Triangulo inexistente'
    else:
        if med1 == med2 and med2 == med3:
            return 'Equilátero'
        elif med1!= med2 and med1!= med3 and med3 != med2:
            return 'Escaleno'
        else:
            return 'Isóceles'


def contar(p, letra):
    cont = 0
    for i in p:
        if letra in i:
            cont += 1
    return cont


def revert(num):
    return num[::-1]


def qnt(n):
    cont = 0
    for i in n:
        if i == '.': break
        cont += 1
    return cont


def jogarMaq():
    jogadas = 'Pedra', 'Papel', 'Tesoura'
    maq = choice(jogadas)
    return maq


def definirJog():



def jogada(a, b):
    if a == b:
        return 'Empate'
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return 'Vitória da máquina'
    elif a == 1 and b == 3:
        return 'Vitória sua'

