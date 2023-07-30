from random import choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
n5 = str(input('Nome do quinto aluno: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print('O aluno escolhido para limpar o quadro foi: {}'. format(escolhido))
