#Melhorando o desafio de progressão aritimética.
"""primero = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primero + (10 - 1) * razao
for c in range(primero, decimo, razao):
    print(c, end=' >> ')"""
#-------------------------------------------- Usando while.
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
c = 0
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} >> ", end='')
    termo += razao
    cont += 1
print("FIM")