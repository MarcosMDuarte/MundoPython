#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# EXISTE UMA PROGRAMAÇÃO MELHOR NO VÍDEO DA AULA

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
somacoluna = 0
cont = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))

print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
print('=-'*30)
for v in matriz:
    #print(v)
    somacoluna += v[2]
    if cont == 1:
        v.sort()
        maior = v[-1]
    cont += 1
    for p in v:
        if p %2 ==0:
            soma +=p
print(f'A soma dos valores pares é {soma}.')
print((f'A soma da terceira coluna é {somacoluna}.'))
print(f'O maior valor da segunda linha é {maior}.')


