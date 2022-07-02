times = ( 'Corinthians', 'Red Bull Bragantino', 'Santos', 'Atlético-MG', 'Coritiba', 'Internacional',
          'Avaí', 'América-MG', 'São Paulo', 'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará',
          'Athletico PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print('-='*20)
print(f'Lista de times do Brasileirão {times}', '\n')
print('-='*20)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-='*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*20)
print(f'Em ordem alfabética {sorted(times)}')
print('-='*20)
print(f"O Internacional está na {times.index('Internacional')+1}º posição")