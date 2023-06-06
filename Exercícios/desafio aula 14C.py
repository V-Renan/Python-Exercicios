from time import sleep
menu = 0
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
while menu != 5:
    soma = v1 + v2
    mult = v1 * v2
    maior = v1
    print("""\033[34m>>>MENU<<<\033[m
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    menu = int(input("Sua opção: "))
    if menu == 1:
        print(f"A soma dos valor {v1} e {v2} é igual a: {soma}")
    elif menu == 2:
        print(f"A multiplicação entre os valor {v1} e {v2} resulta em: {mult}")
    elif menu == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f"O maior valor digitado foi {maior}")
    elif menu == 4:
        print(f"""\033[36mDigite os novos valores abaixo.\033[m""")
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif menu == 5:
        print("\033[33mFINALIZANDO...\033[m")
    else:
        print("\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!!\033[m")
    print("--" * 22)
    sleep(2)
print("Fim do programa, volte sempre!")
