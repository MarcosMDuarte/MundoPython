#pergunte o salario de um funcionário e calcule o aumento
#superior a 1250,00 10%
#inferior ou igual 15%

sal = float(input('Qual o salário do funcionário? R$'))
if sal > 1250.00:
    a = sal+sal*0.10
else:
    a = sal+sal*0.15

print('Com o aumento seu sálrio ficou {}'.format(a))