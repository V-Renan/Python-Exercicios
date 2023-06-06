from math import hypot
Cto = float(input('Comprimento do cateto oposto: '))
Cta = float(input('Comprimento do cateto adjacente: '))
#hip = (Cto ** 2) + (Cta ** 2)
Hip = hypot(Cto, Cta)
print('A hipotenusa vai medir: {:.2f}'. format(Hip))




