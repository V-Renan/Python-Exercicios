cont = 0
somaidade = 0
mulher = 0
total = 0
print('=' *20)
print("CADASTRE UMA PESSOA")
print('='*20)
while True:
    idade = int(input("Qual a sua idade: "))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input("Qual o seu sexo: [M/F] ")).upper()
    total += 1
    if idade > 18:
        somaidade += 1
    if sexo == "M":
        cont += 1
    if sexo == "F":
        if idade < 20:
            mulher += 1
    op = ' '
    while op not in "SN":
        op = str(input("Deseja continuar? ")).upper()
    if op == "N":
        break
print(f"Ao todo foram cadastradas {total} pessoas, {somaidade} são maiores de 18 anos, {cont} pessoas são do sexo Masculino e {mulher} mulheres tem menos de 18 anos.")