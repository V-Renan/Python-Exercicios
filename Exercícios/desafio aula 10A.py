import random
from time import sleep
aleatorio = random.randint(0, 5)
amigo = input(f"Qual o seu nome? ")
msg = (input(f"Olá {amigo.capitalize()}, vamos jogar um jogo? "))
print("Acabei de pensar em um número aleatório, vamos ver se consegue descobrir. ")
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(5)
if jogador == aleatorio:
    print('-=-' * 20)
    print("É exatamente esse número, como você sabia? ")
    print('-=-' * 20)
else:
    print(f"Errou! O número era {aleatorio}, sabia que não iria me vencer!!")
