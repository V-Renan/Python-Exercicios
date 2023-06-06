def ficha(j, g):
    return print(f"O jogador {j} fez {g} gols(s) no campeonato. ")


# programa principal
nome = str(input("Nome do jogador: "))
gols = str(input(f"Quantidade de gols: "))
if nome.strip() == '':
    nome = '<Desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
