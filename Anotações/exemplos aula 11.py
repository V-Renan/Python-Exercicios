# \033[0;33;44m
nome = 'Victor'
cores = {'limpa': '\033[m',
         'roxo': '\033[35m',
         'azul': '\033[36m'}
print(f"Olá mundo, {cores['roxo']}{nome}{cores['limpa']}!!")
