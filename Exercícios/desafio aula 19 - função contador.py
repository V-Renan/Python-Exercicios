from time import sleep


def lin():
    print('-=-' * 20)


def contador(i, f, p):
    lin()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
lin()
