num = (int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))
print(f'Você digitou {num}')
if 9 in num:
    print(f'o valor 9 apareceu {num.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in num:
    print(f'O valor 3 foi difitado na {num.index(3)+1}º posição.')
else:
    print('Não existe o número 3 na tupla.')
print('Os valores pares digitados foram: ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end = ' ')



