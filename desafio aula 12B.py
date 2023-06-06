num = int(input("Digite um número inteiro: "))
print("""Escolha uma opção para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL""")
op = int(input("Sua opção: "))
if op == 1:
    print(f"{num} Convertido para BINÁRIO é igual a: {bin(num)[2:]}")
elif op == 2:
    print(f"{num} Convertido para OCTAL é igual a: {oct(num)[2:]}")
elif op == 3:
    print(f"{num} Convertido para HEXADECIMAL é igual a: {hex(num[2:])}")
else:
    print("Opção inválida, tente novamente.")
#[2:] é para fatiar a string e começar pela terceira casa, pois não quero que comece nem pela posição 0 nem 1
# 0b para o Python sigifica binário.
# 0o para o Python significa octal.
# 0x para o Python significa hexadecimal.