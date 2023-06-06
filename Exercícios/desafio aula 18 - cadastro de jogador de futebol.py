ficha = dict()
gols = list()
ficha['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {ficha['nome'].capitalize()} jogou? "))
for c in range(0, partidas):
    chutes = int(input(f"Quantos gols na partida {c + 1}? "))
    gols.append(chutes)
    ficha['gols'] = gols
    for c in gols:
        ficha['total'] = c + c
print('=-=' * 20)
print(ficha)
print('=-=' * 20)
for k, v in ficha.items():
    print(f"O campo {k} tem o valor {v}.")
print('=-=' * 20)
print(f"O jogador {ficha['nome']} jogou {partidas} partidas.")
for pos, g in enumerate(gols):
    print(f"  => Na partida {pos + 1}, fez {g} gols.")
print(f"Foi um total de {ficha['total']} gols.")
