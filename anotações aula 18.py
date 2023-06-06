#tulpas = ()
#listas = list() ou []
#dicionários = {} ou dict()
'''dados = {'nome':'victor','idade': 23}
print(dados['nome'], dados['idade'])
dados['sexo'] = 'masculino'
print(dados['sexo'])
del dados['idade']
print(dados.values()) #pega todos os valores de (dados)
print(dados.keys()) #pega todas as chaves de (dados)
print(dados.items()) #pega valores e chaves de (dados)
for k, v in dados.items():
    print(f"o {k} é {v}")'''
#-------------------------------------------


"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Paraíba', 'sigla': 'PB'}
brasil.append(estado1)
brasil.append(estado2)
for k, v in brasil[1].items():
    print(f'{k}: {v}')"""
#-------------------------------------------


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} {v}', end=' ')
    print()
