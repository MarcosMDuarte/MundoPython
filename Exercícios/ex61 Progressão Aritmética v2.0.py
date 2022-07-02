'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''


print('='*30)
print('   10 TERMOS DE UMA PA')
print('='*30)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = int(input('Quantos termos você gostaria de visualizar? '))
c = 1
while c <= t:
    print(n, end=' -> ')
    n = n + r
    c +=1
print('Acabou!')