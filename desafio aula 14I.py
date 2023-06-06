cont = soma = media = maior = menor = 0
r = 'S'
while r == 'S':
    n = int(input("Digite um número: "))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    r = str(input("Quer continuar? ")).upper()
print(f"""Você digitou {cont} números. A media dos valores digitado é {media:.2f}
O maior valor digitado foi {maior} e o menor foi {menor}.""")
