n1 = float(input("Quantos km tem a sua viagem? "))
print(f"Você está prestes começar uma viagem de {n1}")
if n1 <= 200:
    preço = n1 * 0.50
else:
    preço = n1 * 0.45
print(f"O preço da sua passagem será de: R${preço:.2f}")

