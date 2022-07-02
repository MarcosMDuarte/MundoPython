#que leia o comprimento de três retas e diga ao susuiário se elas podem ou não formar um triângulo

n1 = float(input('Digite um tamanho de uma reta: '))
n2 = float(input('Digite um tamanho de uma reta: '))
n3 = float(input('Digite um tamanho de uma reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma um Triângulo!!')
else:
    print('Não forma um triângulo!')



'''if n1>n2:
    if n1>n3:
        maior = n1
    else: maior = n3
else:
    if n2>n3:
        maior = n2
    else:
        maior = n3

if maior <= n1 + n2:
    if maior <= n2 + n3:
        print('triângulo')
    else: print('Não')
else:
    print('não')'''
