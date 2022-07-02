exp = str(input('Digite uma expreção: '))
pilha = []
cont_a = cont_f = 0
for s in exp:
    if s == '(':
        cont_a += 1
    if s == ')':
        cont_f += 1
if cont_a == cont_f:
    print('Expressão válida.')
else:
    print('Expressão inválida!')