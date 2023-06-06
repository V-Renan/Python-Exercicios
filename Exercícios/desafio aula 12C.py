n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
if n1 > n2:
    maior = n1
    print(f"O número {n1} é o primeiro valor e é maior.")
elif n2 > n1:
    maior = n2
    print(f"O número {maior} é o segundo valor e é maior.")
else:
    print(f"Os valores {n1} e {n2} são iguais. ")

