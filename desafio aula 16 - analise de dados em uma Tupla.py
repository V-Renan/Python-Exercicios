n1 = (int(input("Digite um número: ")),int(input("Digite outro número: ")),
      int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print(f"O número 9 apareceu {n1.count(9)} vezes.")
if 3 in n1:
    print(f"O número primeiro número 3 foi digitado na {n1.index(3, 0)+1}ª posição.")
else:
    print("O número 3 não foi digitado nenhuma vez.")
print(f"Os valores pares digitados foram ", end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
