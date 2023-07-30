r = float(input('Quer comprar dolar ou euro? \nDigite o valor em reais e descubra quanto você pode comprar: R$'))
dol = r / 5.15
euro = r / 5.46
print('Com R${:.2f} você pode comprar {:.2f} US$. Ou €{:.3f}'.format(r, dol, euro))
