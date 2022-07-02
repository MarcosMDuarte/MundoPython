'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

num = []
for c in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menorvalor = maiorvalor = num[c]
    else:
        if num[c] > maiorvalor:
            maiorvalor = num[c]
        if num[c] < menorvalor:
            menorvalor = num[c]


print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maiorvalor} nas posições', end= ' ')
for i, v in enumerate(num):
    if v == maiorvalor:
        print(f'{i}...', end=' ')

print(f'\no menor valor digitado foi {menorvalor} nas posições', end= ' ')
for i, v in enumerate(num):
    if v == menorvalor:
        print(f'{i}...', end=' ')