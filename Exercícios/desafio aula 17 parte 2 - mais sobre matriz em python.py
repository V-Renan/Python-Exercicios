matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = coluna = 0
for lin in range(0, 3):
    for c in range(0, 3):
        matriz[lin][c] = int(input(f"Digite um valor para {lin, c}: "))
print('-=-' * 20)
for lin in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[lin][c]:^5}]", end='')
        if matriz[lin][c] % 2 == 0:
            somapar += matriz[lin][c]
    print()
print('-=-' * 20)
print(f"A soma dos valores par é: {somapar}")
for lin in range(0, 3):
    coluna += matriz[lin][2]
print(f"A soma da terceira coluna é: {coluna}")
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é: {maior}")
