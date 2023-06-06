salario = float(input("Qual o seu salário atual? "))
if salario >= 1250:
    novo = salario * 10 / 100
    print(f"Seu salário com um aumento de 10% é: R${salario + novo:.2f}")
else:
    novo = salario * 15 / 100
    print(f"Seu salário com um aumento de 15% é: R${salario + novo:.2f}")



