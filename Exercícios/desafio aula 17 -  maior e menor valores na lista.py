maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=='*20)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} nas posições: ", end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f"{p}... ", end='')
print()
print(f"O menor valor digitado foi {menor} nas posições: ", end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f"{p}... ", end='')
print()
