nome = input('Nome: ').upper()
cargo = input('Cargo :(1) Professor (2) Coordenador (3) Zelador: ').upper()
if cargo == '1':
  cargo ='Professor'
elif cargo == '2':
  cargo = 'Coordenador'
elif cargo == '3':
  cargo = 'Zelador'
salario = float(input('Salário: '))
ns = salario * 1.10
boni = ns * 0.05
if ns + 1049 >= 4987:
  if ns > 4987:
    irrf = 0.275
  else:
    irrf = 0.225
elif ns + 971 >=3938:
  irrf = 0.15
elif ns + 968 >= 2967:
  irrf = 0.075
else:
  irrf = 0
irrf = ns *irrf
print(f'''Colaborador: {nome}
Cargo: {cargo}
Salário Novo: {ns:.2f}
Bonificação: {boni:.2f} R$
IRRF: {irrf:.2f} R$
Salário Líquido: {ns+boni-irrf:.2f} R$''')