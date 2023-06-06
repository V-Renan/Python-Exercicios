lista = [[], [], []]
for cont1 in range(0, 3):
    lista[0].append(int(input(f"Digite um valor para [0, {cont1}]: ")))
for cont2 in range(0, 3):
    lista[1].append(int(input(f"Digite um valor para [1, {cont2}]: ")))
for cont3 in range(0, 3):
    lista[2].append(int(input(f"Digite um valor para [2,  {cont3}]: ")))
print('-=-' * 20)
print(f"[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]")
print(f"[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]")
print(f"[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]")
print("FIM DO PROGRAMA!")
