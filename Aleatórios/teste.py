brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Paraíba', 'sigla': 'PB'}
brasil.append(estado1)
brasil.append(estado2)
for k, v in brasil[0].items():
    print(f'{k}: {v}')
