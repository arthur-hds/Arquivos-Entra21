from random import randint
def situacao(nome, nota):
    if nota >= 7.5:
        sit = "Aprovado"
    else:
        sit = "Reprovado"
    d = {
        "Aluno": nome,
        "Nota" : nota,
        "Situação" : sit
    }
    return d

def Jogar4(J1, J2, J3, J4):
    for i in Jogar4:
        print(i)