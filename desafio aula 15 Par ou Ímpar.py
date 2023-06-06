from random import randint
v = 0
print("Consegue me vencer no par ou ímpar? ")
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. total {total}.")
    if tipo == "P":
        if total % 2 == 0:
            print("VOCÊ VENCEU!!")
            v += 1
        else:
            print("COMPUTADOR VENCEU!!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("VOCÊ VENCEU!!!")
        else:
            print("COMPUTADOR VENCEU!!!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER. VOCÊ VENCEU {v} VEZES!")
