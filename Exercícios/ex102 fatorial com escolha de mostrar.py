def fatorial(n, show=False):
    '''
    -> calcula o Fatorial de um número
    :param n: o numero a ser calculado
    :param show:  (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    '''

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' X ', end='')
            else:
                print('= ', end= '')
        f *= c
    return f




print(fatorial(5))