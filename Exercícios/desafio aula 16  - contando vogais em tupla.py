lista = ('dinheiro', 'trabalho', 'demostrativo', 'aguento', 'socorro')
vogais = ('a', 'e', 'i', 'o', 'u')
contador = 0
for c in lista:
    print(f"\nNa palavra {c} temos >>> ", end='')
    for letra in c:
        if letra in vogais:
            print(letra, end=' ')