from datetime import date
nasc = int(input("Qual o seu ano de nascimento? "))
year = date.today().year
idade = year - nasc
print(f"Você nasceu em {nasc} e tem {idade} anos em {year}.")
if idade < 18:
    saldo = 18 - idade
    ano = year + saldo
    print(f"""Você tem menos de 18 anos, por isso não será necessário se alistar neste ano de {year}.
Seu alistamento será em {ano}. """)
elif idade == 18:
    print(f"Neste ano de {year}, você completa 18 anos e deve se alistar no serviço militar, procure a prefeitura da sua cidade!")
elif idade > 18:
    saldo = idade - 18
    ano = year - saldo
    print(f"Você perdeu seu praso de alistamento, deveria ter se alistado em {ano}, procure a prefeitura da sua cidade e regularize seus documentos.")
