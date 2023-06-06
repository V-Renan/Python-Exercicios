lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input("Digite qualquer número: ")))
    r = str(input("Quer continuar? ")).upper().strip()[0]
    if r == 'N':
        break
for n in lista1:
    if n % 2 == 0:
        par = n
        lista2.append(par)
    elif n % 2 == 1:
        impar = n
        lista3.append(impar)
print('===' * 20)
print(f"""A lista completa é: {lista1}
A lista de números pares é: {lista2}
A lista de números ímpares é: {lista3}""")
print("Programa encerrado!")
