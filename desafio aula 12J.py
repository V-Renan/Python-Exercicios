from random import choice
from time import sleep
cores = {'azul': '\033[34m',
         'vermelho': '\033[31m',
         'limpa': '\033[m'}
print('\033[31m' '-=-' '\033[m' * 20)
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista).upper()
x1 = input("Pedra, Papel ou Tesoura? ").upper()
print('\033[31m' '=-=' '\033[m' * 20)
print(f"""Computador jogou: {computador}
Você jogou: {x1}""")
print("ANALISANDO....")
sleep(1)
if computador == 'PEDRA':
    if x1 == 'PEDRA':
        print("EMPATE!!")
    elif x1 == 'PAPEL':
        print("Você venceu!!")
    elif x1 == 'TESOURA':
        print("Computador vence!!")
    else:
        print("Jogada inválida!")
if computador == 'PAPEL':
    if x1 == 'PEDRA':
        print("Computador vence!!")
    elif x1 == 'PAPEL':
        print("EMPATE!!")
    elif x1 == 'TESOURA':
        print("Você venceu!!")
    else:
        print("Jogada inválida!")
if computador == 'TESOURA':
    if x1 == 'PEDRA':
        print("Você venceu!!")
    elif x1 == 'PAPEL':
        print("Computador vence!!")
    elif x1 == 'TESOURA':
        print("EMPATE!!")
    else:
        print("Jogada inválida!")
