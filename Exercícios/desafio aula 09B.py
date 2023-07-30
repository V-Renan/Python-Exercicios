num = int(input('Digite um número: '))
#n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
'''print('Analisando o número {}...'.format(num))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u,d,c,m))'''
print(f'Analisando o numero {num}')
print(f'''Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}''')
