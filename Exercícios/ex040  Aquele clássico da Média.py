'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, sua média é {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print("Média abaixo de 5.0: REPROVADO")
elif media > 5.0 and media < 6.9:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print('Média 7.0 ou superior: APROVADO')
