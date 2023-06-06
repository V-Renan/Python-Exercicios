produto = float(input("Qual o valor do produto? R$ "))
print("""Qual a forma de pagamento desejada?
À vista no dinheiro/cheque com 10% de desconto: [1]
À vista no cartão com 5% de desconto: [2]
Em até 2x no cartão: [3]
3x ou mais no catão com 20% de juros: [4]""")
pag = float(input("Qual a sua opção? "))
if pag == 1:
    total = produto - (produto * 10 / 100)
    print(f"Seu produto de R${produto:.2f} vai custar R${total:.2f}")
if pag == 2:
    total = produto - (produto * 5 / 100)
    print(f"Seu produto de R${produto:.2f} vai custar R${total:.2f}")
if pag == 3:
    total = produto / 2
    print(f"Seu produto de R${produto:.2f} será de duas parcelas de R${total:.2f}")
if pag == 4:
    total = produto + (produto * 20 / 100)
    totalparcel = int(input("Quantas parcelas? "))
    parcela = total / totalparcel
    print(f"""Sua compra será parcelada em {totalparcel}x de R${parcela:.2f} COM JUROS.
Sua compra de R${produto:.2f} vai custar R${total:.2f} no final.""")
else:
    total = 0
    print(f"""\033[31mOpção INVÁLIDA de pagamento. Tente novamente!\033[m
Sua compra de R${produto:.2f} vai custar R${produto:.2f} no final.""")

