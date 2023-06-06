# Funções ==> Rotin -------------- def ==> definição de função
'''def lin():
    print('-' * 30)


def mensagem(msg):
    lin()
    print(msg)
    lin()


mensagem('SISTEMA DE ALUNOS')
mensagem('NOTAS DO ALUNO')
mensagem('SITUAÇÃO DO ALUNO')'''



def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")


# PROGRAMA PRINCIPAL
soma(a=5, b=4) # para deixar claro quem é A e B
print('--' * 30)


def contador(*num):
    #for valor in num:
        #print(f'{valor} ', end='')
    #print("FIM!")
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('===' * 30)
def soma(* valores): # desempacotar somando
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")


print()
print('===' * 30)




def dobra(lst):
    print("Dobrando em lista")
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


