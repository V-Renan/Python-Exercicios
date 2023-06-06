lista = []
while True:
    lista.append(int(input("Digite um número qualquer: ")))
    r = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if r in 'N':
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} valores. ")
print(f"Os valores digitados em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi digitado.")