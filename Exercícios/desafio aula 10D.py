n1 = float(input("Quantos km tem a sua viagem? "))
print(f"Você está prestes começar uma viagem de {n1}")
if n1 <= 200:
    preco = n1 * 0.50
else:
    preco = n1 * 0.45
print(f"O preço da sua passagem será de: R${preco:.2f}")
