from datetime import datetime
pessoas = dict()
data = datetime.now().year
pessoas['Nome:'] = str(input("Nome: "))
ano = int(input("Ano de  Nascimento: "))
pessoas['Idade:'] = data - ano
pessoas['CTPS:'] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoas['CTPS:'] != 0:
    pessoas['Inicio do Contrato:'] = int(input("Ano de Contratação: "))
    pessoas['Salário:'] = float(input("Salário: R$"))
    pessoas['Aposentadoria:'] = pessoas['Idade:'] + pessoas['Inicio do Contrato:'] + 35 - datetime.now().year
print('-=-' * 20)
for k, v in pessoas.items():
    print(f"  - {k} {v}")
print('Finalizando programa!')
