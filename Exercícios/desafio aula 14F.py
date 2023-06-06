primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
op = 10
while op != 0:
    total += op
    while cont <= total:
        print(f"{termo} >> ", end='')
        termo += razao
        cont += 1
    print("...")
    op = int(input("""Quantos termos você quer mostrar a mais? """))
print(f"foram exibidos um total de {total} resultados de PA.")
