from time import sleep
c = ('\033[m',        # 0 - Sem cor
    '\033[0;30;41m', # 1 -vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azull
    '\033[0;30;45m', # 5 - roxo
    '\033[7;0;30m'     # 6 -  branco
     );


def ajuda(a):
    título(f'Acessando o manunal do comando \'{a}\'', 4)
    print(c[2], end='')
    help(a)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg} ')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


while True:
    título('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!!', 1)