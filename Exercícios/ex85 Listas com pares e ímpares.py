#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
#numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
total = [[], []]
for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    if num %2 == 0:
        total[0].append(num)
    else:
        total[1].append(num)
total[0].sort()
total[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram {total[0]}')
print(f'Os valores ímpares digitados foram {total[1]}')