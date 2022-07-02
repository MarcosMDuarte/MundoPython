'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

print('='*30)
print('   10 TERMOS DE UMA PA')
print('='*30)

n = int(input('Primeiro termo:'))
r = int(input('Razão:'))
d = n + (10 - 1) * r

for c in range(n,d+r,r):
    print(c, end=' -> ')

print('Acabou!')