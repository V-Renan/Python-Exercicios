from time import sleep
from random import randint
lista = []
jogos = []
print('-' * 30)
print('          MEGA SENA     ')
print('-' * 30)
op = int(input("Quantos jogos você quer que eu sorteie?\n"))
print(f"{'-=-' * 5}{f'SORTEANDO {op} JOGOS'}{'-=-' * 5}")
total = 1
while total <= op:
    cont = 0
    while True:
        aleatorio = randint(0, 60)
        if aleatorio not in lista:
            lista.append(aleatorio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for pos, c in enumerate (jogos):
    sleep(1)
    print(f"Jogo {pos + 1}: {c}")
