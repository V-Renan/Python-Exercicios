import math
km = float(input("A quantos km/h o seu carro está? "))
multa = (km - 80) * 7.00
if km >= 81:
    print(f"Você está a {km}km/h, acima da velocidade permitida na via. Por isso receberá uma multa equivalente a: R${multa:.2f}")
else:
    print("Seu carro está a {km}km/h que é velocidade permitida pela via, por isso não receberá multa.")

