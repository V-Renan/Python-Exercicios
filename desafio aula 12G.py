r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
#triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f"Considerando as retas {r1:.0f}, {r2:.0f} e {r3:.0f}, o triângulo formado é ", end='')
    if r1 == r2 == r3:
        print("EQUILÁTERO!!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!!")
    else:
        print("ISÓSCELES!!")
else:
    print(f"Considerando as retas {r1:.0f}, {r2:.0f} e {r3:.0f}, não é possível formar um triângulo. ")
# end='' significa que n vai ter fim da linha e vai adicionar a de baixo.