def notas(*valor, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param valor: Uma ou mais notas de alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    alunos['total'] = len(valor)
    alunos['maior'] = max(valor)
    alunos['menor'] = min(valor)
    alunos['media'] = sum(valor)/len(valor)
    if sit:
        if alunos['media'] > 6:
            alunos['sit'] = 'BOA'
        elif alunos['media'] >= 5:
            alunos['sit'] = 'RAZOÁVEL'
        else:
            alunos['sit'] = 'RUIM'
    return alunos


# programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
