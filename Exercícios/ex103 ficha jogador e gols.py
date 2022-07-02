def ficha(nome='desconhecido', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato. ')

n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

ficha(n, g)
