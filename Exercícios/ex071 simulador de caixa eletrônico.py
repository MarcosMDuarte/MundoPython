'''Exercício Python 071: Crie um programa que simule o funcionamento de um
caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("="*15)
print('   BANCO CEV')
print("="*15)
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    if valor >= 50:
        cont50 += 1
        valor = valor - 50
    else:
        break
while True:
    if valor >= 20:
        cont20 += 1
        valor = valor - 20
    else:
        break
while True:
    if valor >= 10:
        cont10 += 1
        valor = valor - 10
    else:
        break
while True:
    if valor >= 1:
        cont1 += 1
        valor = valor - 1
    else:
        break
if cont50 != 0:
    print(f'Total de {cont50} cédulas de R$50,00')
if cont20 != 0:
    print(f'Total de {cont20} cédulas de R$20,00')
if cont10 != 0:
    print(f'Total de {cont10} cédulas de R$10,00')
if cont1 != 0:
    print(f'Total de {cont1} cédulas de R$1,00')
print('='*15)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')