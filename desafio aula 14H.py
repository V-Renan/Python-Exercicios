cont = soma = 0
n = int(input("Digite um valor: "))
num = n
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um valor: "))
print(f"foram digitados {cont} valores e sama entre eles é {soma}")
