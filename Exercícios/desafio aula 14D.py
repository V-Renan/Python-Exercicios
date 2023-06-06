#Usando import factorial.
"""from math import factorial
n = int(input("Digite um número inteiro: "))
c = 1
f = factorial(n)
print(f"O fatorial de {n} é {f}")"""
#-------------------------------------------------------
#Calculo manual usando while.
"""from time import sleep
n = int(input("Digite um número inteiro: "))
c = n
f = 1
print(f"Calculando {n}! = ", end='')
sleep(1)
while c > 0:
    print(c, end='')
    print(" x " if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)"""
#----------------------------------------------------------
#Calculo manual usando for.
n = int(input(">>> Digite um valor para calular seu Fatorial: "))
c = 0
f = 1
for c in range(n - 1, c - 1, -1):
    c += 1
    print(c, end='')
    print(" x " if c > 1 else ' = ', end='')
    f *= c
print(f"{f}")


