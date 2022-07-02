#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


ficha = {}
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))

if ficha['Média'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['Média'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
print('-+'*30)
for k, v in ficha.items():
    print(f'{k} é igual a {v}')
print('-+'*30)