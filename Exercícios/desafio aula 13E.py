s = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite um número intero: "))
    if n % 2 == 0:
        s += n
        cont += 1
print(f"A soma dos {cont} números pares solicitados é igual a: {s} ")

