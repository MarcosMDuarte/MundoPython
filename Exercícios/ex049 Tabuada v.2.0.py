'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que
 o usuário escolher, só que agora utilizando um laço for.'''


'''n = int(input('Digite um número inteiro: '))
print('~'*15)
for c in range (1,11):
        print('  {} X {} = {}'.format(n, c, n*c))'''


lista = [1]
for c in range(0,7):
    print(lista)
    lista.append(lista[c]+1)



