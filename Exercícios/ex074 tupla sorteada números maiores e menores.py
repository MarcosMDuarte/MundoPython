from random import randint
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), )
print(f'Os valores sorteados foram :', end=' ')
for cont in n:
    print(cont, end= ' ')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')


