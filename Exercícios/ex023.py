# faça um programa que leia um número de 0 a 9999 e nostre na tela cada um dos digitos separados.

#ex::
#digite um Número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

num = int(input('Digite um número de 0 até 9999: '))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('O número digitado é: {}.\nA unidade é: {}.\nA dezena é: {}.\nA centena é: {}.\nO milhar é: {}.'.format(num,uni,dez,cen,mil))