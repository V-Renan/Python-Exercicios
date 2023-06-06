total = 0
r = ' '
while True:
    valor = int(input("Valor: "))
    total += valor
    r = str(input("Deseja continuar? ")).strip().upper()[0]
    if r == "N":
        break
print(f"O total é igual a: R${total:.2f}")
