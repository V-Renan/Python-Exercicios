#for c in range(0, 6): #Vai contar de 1 até 5. Para contar de 1 até 6 tem que usar o 7, pq o Python ignora a última casa.
    #print(c)
#print("fim")
#for c in range(6, 0, -1): #Vai contar de 6 até zero tirando 1.
#for c in range(0, 7, 2): #Vai contar de zero até 7 pulando duas casas.
'''n = int(input("Digite um número: "))
for c in range(1, n+1): #Vai contar de 1 até (n) + 1.
    print(c)
print("fim")'''


"""i = int(input("Início: "))
f = int(input("Final: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("fim")"""

s = 0
for c in range(0, 3): #Vai pedir o valor do input três vezes.
    n = int(input("Digite um valor: "))
    s += n
print(f"O somatório dos valores é igual a: {s}")