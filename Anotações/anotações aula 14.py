# while p/ português é ENQUANTO.
total = 0
totali = 0
n = 0
r = 'S'
while r == "S":
    n = int(input("Digite um número: "))
    r = str(input("Deseja continuar? [S/N] ")).upper()
    if n != 0:
        if n % 2 == 0:
            total += 1
        else:
            totali += 1
print(f"""Foram ao todo {total} números PARES.
E {totali} números ÍMPARES.""")
print("fim")
