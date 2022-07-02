itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Livro', 34.90 )

print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)

for cont in range(0, len(itens), 2):
    print(f'{itens[cont]:.<30}', end= ' ')
    print(f'R${itens[cont+1]:>7.2f} ')

print('-'*40)

'''
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'R${itens[pos]:.<30}', end='')
    else: 
        print(f'R${itens[pos]:>7f}')
'''