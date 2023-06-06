nome = str(input("Qual o seu nome? ")).upper()
idade = int(input("Qual sua idade? "))
sexo = str(input("Qual o seu sexo? ")).strip().upper()[0]
while sexo not in 'fFmM':
    print("Opção inválida, tente novamente!!")
    sexo = str(input("Qual o seu sexo? ")).strip().upper()[0]
    if sexo =='Ff':
        sexo = 'FEMININO'
    elif sexo == 'Mm':
        sexo = 'MASCULINO'
print(f"Seu nome é {nome.capitalize()}, você tem {idade} anos, e é do sexo {sexo}.")
