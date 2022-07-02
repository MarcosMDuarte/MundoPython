n = str(input('Digite uma expressão: '))
lista = []
for sim in n:
    if sim == '(':
        lista.append(sim)
    else:
        if len(lista) == 0:
            lista.append(sim)
            break
        else:
            lista.pop()
if len(lista) == 0:
    print('Expressão correta')
else:
    print('Expressão errada!')
