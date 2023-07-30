p = float(input('Qual o preço do produto? '))
novo = p - (p*5/100)
print('O produto que custava R${:.2f}, na promoção por 5% vai custar R${:.2f}.'.format(p, novo))
