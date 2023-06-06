casa = float(input("Qual o valor do imóvel? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Em quantos anos você deseja pagar o imóvel? "))
porcentagem = salario * 30 / 100
#parcela = casa / (anos * 12)
parcela = (casa / anos) / 12
if parcela <= porcentagem:
    print(f"""Durante {anos} anos, o valor da sua prestação mensal será de: R${parcela:.2f}
Empréstimo CONCEDIDO!""")
else:
    print(f"O valor da parcela será de {parcela:.2f}, irá exceder os 30% do seu salário, por este motivo você não poderá fazer esse empréstimo. ")
