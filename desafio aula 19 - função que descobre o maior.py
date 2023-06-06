from time import sleep


def lin():
    print('--' * 20)


def maior(*num):
    maior = cont = 0
    lin()
    print('Analisando os valores passados... ')
    for valor in num:
        print(f"{valor} ", end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")


# Programa principal
maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
