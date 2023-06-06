from datetime import date
ano = date.today().year
total = 0
totalm = 0
for c in range(1, 7):
    nasc = int(input(f"Em qual ano a {c}ª pessoa nasceu? "))
    idade = ano - nasc
    if idade >= 21:
        total += 1
    else:
        totalm += 1
print(f"""Ao todo tivemos {total} pessoas maiores de idade.
Também tivemos {totalm} pessoas menores de idade. """)