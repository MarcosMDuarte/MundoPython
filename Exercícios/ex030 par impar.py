#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

n = int(input('Digite um número inteiro: '))

num = n%2

if num == 0:
    print('{} é um número par'.format(n))
else:
    print('{} é um número é impar'.format(n))