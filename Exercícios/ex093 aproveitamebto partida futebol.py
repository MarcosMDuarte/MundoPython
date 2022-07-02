ficha = {}
ficha['nome'] = str(input('Nome do Jogador: '))
part = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
cont = 0
gol = []
total = 0
while cont < part:
    gols = int(input(f'Quantos gols na {cont+1}º partida? '))
    gol.append(gols)
    cont += 1
    total += gols

ficha['gols'] = gol[:]
ficha['total'] = total
print('-='*30)
print(ficha)
print('-='*30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O Jogador {ficha["nome"]} jogou {part} partidas.')

teste = 0
for c in ficha['gols']:
    print(f'=> Na partida {teste}, fez {ficha["gols"][teste]} gols.')
    teste += 1
print(f'Foi um total de {ficha["total"]} gols.')
