nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Em letras maiúsculas: {}'.format(nome.upper()))
print('Em letras minúsculas: {}'.format(nome.lower()))
print('Tem um total de {} caracteres'.format(len(nome)-(nome.count(' '))))
novo = (nome.split())
print('O primeiro nome tem {} letras.'.format(len(novo[0])))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))







