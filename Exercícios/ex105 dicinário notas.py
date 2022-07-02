def notas(*n, sit=False):
    '''
    -> Função para analisar notas e sintuações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionara situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    ficha ={}
    ficha['tortal'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['média'] = sum(n)/len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        elif ficha ['média'] >= 5:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'
    return ficha



#programa principaç

resp = notas(5.5, 2.5, 9, 1.5, sit=True)

print(resp)
help(notas)