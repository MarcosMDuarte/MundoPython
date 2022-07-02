'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

contmaior = conthom = contmul = cont = 0

while True:
    print('-' * 30)
    if cont == 0:
        print('    CADASTRE UMA PESSOA')
    else:
        print('    CADASTRE OUTRA PESSOA')
    cont += 1
    print('-' * 30)
    i = int(input('Idade: '))
    if i > 18:
        contmaior += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if s == 'M':
        conthom += 1
    elif i > 20:
        contmul += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
        
print(f'Total de pessoas com mais de 18 anos: {contmaior}')
print(f'Ao todo temos {conthom} home', end='')
print('m' if conthom == 1 else 'ns', end=' ')
print('cadastrado', end='')
print('.' if conthom == 1 else 's.')
print(f'E temos {contmul} mulher', end='')
print(' ' if contmul == 1 else 'es ', end='')
print('com menos de 20 anos.')