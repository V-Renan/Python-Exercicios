#            VARIAVEIS COMPOSTAS [LISTA]
'''comida = ['hamburguer', 'suco','pizza', 'pudim']
comida[3] = 'picole' # substitui o pudim pelo picole
comida.append('coockie') #adiciona o coockie no final da lista
comida.insert(0,'cachorro-quente') # adiciona o cachorro quente antes do hamburguer, (ou em qualquer posição desejada)
comida.remove('coockie') #apaga o elemento da lista ('remove' procura do inicio e vai remover o primeiro )
del comida[2] #elimina o elemento 3 dentro da lista
comida.pop()# normalmente o pop elimina o último elemento, mas pode ser usado indicando a posição do elemento
for p in comida:
    print(p)'''

"""if 'pizza' in comida:
    lanche.remove('pizza')"""

    # CRIANDO ESTRUTURA DE VALORES
"""valores = list(range(4, 11))
    print(valores)"""

valores = [8, 2, 5, 4, 9, 3, 0]
(valores.sort())
print(valores)
#valores.sort(reverse=True)# contagem ao contrario
#len(valores)


"""valores = list()
for cont in range(0, 3):
    valores.append(int(input("Digite um valor:\n")))
for pos, v in enumerate(valores):
    print(f"Na posição {pos + 1} encontrei o valor {v}!")"""



# listar A e B
"""a = [2, 3, 4, 7]
b = a
b[2] = 8            #alterar na lista b na posição 2 para o número 8 (em python vai alterar a lista a e b pois se cria uma ligação)          
#para fazer (b) receber uma copia de (a) é necessario usar o seguinte b =a[:] 
#assim b recebera todos os valores de a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""
