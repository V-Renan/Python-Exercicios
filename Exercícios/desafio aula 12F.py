from datetime import date
print('-=-' * 20)
print("Olá, somos da Confederação Nacional de Natação!!")
print('-=-' * 20)
cores = {'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
atual = date.today().year
nasc = int(input("Digite seu ano de nascimento e descubra em qual categoria você se encaixa: "))
idade = atual - nasc
if idade <= 9:
    print(f"Você tem {cores['azul']}{idade}{cores['limpa']} anos e se encaixa na categoria: {cores['azul']}MIRIM{cores['limpa']}")
elif idade <= 14:
    print(f"Você tem {cores['azul']}{idade}{cores['limpa']} anos e se encaixa na categoria: {cores['azul']}INFANTIL{cores['limpa']}")
elif idade <= 19:
    print(f"Você tem {cores['azul']}{idade}{cores['limpa']} anos e se encaixa na categoria: {cores['azul']}JUNIOR{cores['limpa']}")
elif idade <= 25:
    print(f"Você tem {cores['azul']}{idade}{cores['limpa']} anos e se encaixa na categoria: {cores['azul']}SÊNIOR{cores['limpa']}")
else:
    print(f"Você tem {cores['azul']}{idade}{cores['limpa']} anos e se encaixa na categoria: {cores['azul']}MASTER{cores['limpa']}")
