'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

print('-'*30)
print('      LOJA SUPER BARATÃO          ')
print('-'*30)
total = premen = cont = c = 0
prodmen = ' '
while True:
    nom = str(input('Nome do Produto: '))
    pre = int(input('Preço: R$'))
    total += pre
    if pre > 1000:
        cont += 1
    res = ' '
    if c == 0 or pre < premen:
        prodmen = nom
        premen = pre
    c += 1
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {prodmen} que custa R${premen:.2f}')
