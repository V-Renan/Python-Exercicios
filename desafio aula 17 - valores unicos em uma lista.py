valor = list()
while True:
    n = (int(input("Digite um valor: ")))
    if n not in valor:
        valor.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado não será adcionado!")
    r = ' '
    while r not in 'SN':
        r = str(input("Quer continuar? ")).strip().upper()[0]
    if r == 'N':
        break
valor.sort()
print(f"Você digitou os valores {valor}")
print("PROGRAMA ENCERRADO!")
