cont = soma = menor = maior = 0
barato = ' '
contproduto = 0
print('---'*20)
print("LOJA DO GATO MIANDO")
print('---'*20)
while True:
    produto = str(input("Nome do produto: "))
    valor = int(input("Preço: "))
    op = ' '
    while op not in "SN":
        op = str(input("Quer continuar? ")).strip().upper()[0]
    cont += 1
    soma += valor
    if valor > 1000:
        contproduto += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    if op == 'N':
        break
print(f"""O total da compra foi R${soma:.2f} 
{contproduto} custando mais de 1000 reais.
O produto mais barato foi {barato.capitalize()} que custa R${menor:.2f}""")
print("PROGRAMA FINALIZADO!")
