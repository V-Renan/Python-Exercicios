salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15%, passa a receber R${:.2f}.'. format(salario, aumento))
