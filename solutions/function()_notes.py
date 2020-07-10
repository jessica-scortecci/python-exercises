def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :para n: uma ou mais notas dos alunos (aceita várias).
    :para sit: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif 5 <= r['Média'] < 7:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 4.5, sit=True)
print(resp)
#help(notas)
