import random
p = float(input('Qual o preço do produto? '))
desconto = float(input('Qual a porcentagem de desconto? '))
novo = p - (p*desconto/100)
print ('O produto que custava R${}, com {}% de desconto, passa a custar R${:.2f}. '. format(p,desconto, novo))
