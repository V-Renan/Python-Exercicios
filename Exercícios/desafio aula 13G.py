n = int(input("Digite um número inteiro: "))
total = 0
for c in range(1, n + 1):
   if n % c == 0:
      print('\033[34m', end=' ')
      total += 1
   else:
      print('\033[31m', end=' ')
   print(f'{c}', end=' ')
print(f"""\033[m
O número {n} foi dividido {total} vezes.""")
if total == 2:
   print(f"Por isso o número {n}, é primo.")
else:
   print(f"{n} Não é um número primo.")