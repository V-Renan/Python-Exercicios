print("BEM VINDO(A) AO BANCO URUBU!!")
valor = int(input("Quanto você quer sacar?\nR$ "))
total = valor
totalced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"Você vai sacar {totalced} cédulas de R${ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print("FIM DO PROHGRAMA!")
