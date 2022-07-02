from datetime import date
from datetime import datetime # outra maneira de fazer o ano atual segundo o professor
# ano_digitado = int(input('Qual ano você nasceu? '))
# ano_atual_professor = datetime.now().year - ano_digitado
# print(ano_atual_professor)


ficha = {}
atual = date.today().year
while True:
    ficha['Nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    ficha['idade'] = atual - ano
    ficha['ctps'] = int(input('Carteira de Trabalho: (0 não tem)'))
    if ficha['ctps'] == 0:
        break
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salalario'] = float(input('Salártio: '))
    ficha['aposentadoria'] = (35 - (atual - ficha['contratação']))+ficha['idade']
    break

for k, v in ficha.items():
    print(f'- {k} tem o valor {v}')

