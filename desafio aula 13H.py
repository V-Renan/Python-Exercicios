n = str(input("Digite seu nome: ")).strip().upper()
palavras = n.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {n} é {inverso}")
if inverso == junto:
    print(f"A frase (\033[34m{n.capitalize()}\033[m) É UM POLÍNDROMO!")
else:
    print(f"A frase (\033[31m{n.capitalize()}\033[m) NÃO É UM POLÍNDROMO!")


