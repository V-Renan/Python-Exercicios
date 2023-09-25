from datetime import date
ano = int(input("Qual ano você deseja análisar? Digite 0 para análsiar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} É sim um ano Bissexto!")
else:
    print(f"{ano} Não é um ano Bissexto.")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
print(f"[A] tem o valor de: {a} e [B] tem o valor de {b} ")