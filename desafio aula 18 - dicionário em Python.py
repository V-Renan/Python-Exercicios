aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Média: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    print("Situação é igual Reprovado!")
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
