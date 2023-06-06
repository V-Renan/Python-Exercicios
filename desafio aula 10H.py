r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Analisando as retas {r1}, {r2}, {r3}, é sim possível formar um triângulo.")
else:
    print(f"Análisando as retas {r1}, {r2}, {r2}, não é possível formar um triângulo.")
