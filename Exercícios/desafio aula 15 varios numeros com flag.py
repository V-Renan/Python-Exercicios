n = s = cont = 0
while n != 999:
    n = int(input("Digite um valor >> (999 para parar)\n >>> "))
    if n == 999:
        break
    cont += 1
    s += n
print(f"Foram digitados {cont} valores e soma de todos é igual a {s}!")
