lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
#           0            1       2         3
#           -4          -3      -2        -1
#print(sorted(lanche)_ coloca a tupla em ordem
#print(lanche[1:3]) vai escrever do elemento 1 até três, eliminando o três

#----------------------------------------------------------#
#for comida in lanche:
   #print(f"Eu vou comer {comida}.")


#for pos, comida in enumerate(lanche):
    #print(f"Eu vou comer {comida} na posição {pos}")


for comida in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[comida]}")

#-----------------------------------------------------------#

#TUPLAS SÃO IMUTÁVEIS
#TUPLAS PODEM SER CRIADAS COM (), {}, [] OU APENAS COM ASPAS

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5)) >>>>>>>>>>>> vai contar quantas vezes o número 5 aparece em (c)
print(c.index(5)) >>>>>>>>>>>> vai mostrar em qual posição está o número 5
print(c.index(5, 4)) >>>>>>>>> vai mostrar em qual posição está o número 5 a partir da posição 4
'''


#pessoa = ('victor', 23, 'M', 62.00)
#del(pessoa) # Del vai ser usado para apagar a tupla
#print(pessoa)
