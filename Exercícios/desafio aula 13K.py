somaidade = 0
mulher = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    pessoa = str(input("Nome: ")).upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    somaidade += idade
    if p and sexo == 'F':
        if idade < 20:
            mulher += 1
    if pessoa and sexo == 'M':
        velho = idade
        nome = pessoa
        if velho == idade:
            nome = pessoa
        else:
            if velho > idade:
                nome = pessoa
print(f"""Ao todo são {mulher} mulheres com menos de 20 anos.
A média de idade entre as 4 pessoas é de {somaidade / 4} anos.
O homem mais velho tem {velho} e se chama {nome.capitalize()}.""")
