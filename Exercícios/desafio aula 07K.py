dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = float(dias * 60) + (km * 0.15)
print('O total a pagar é: R${:.2f}'. format(pago))
