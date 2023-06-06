print('==='*20)
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{c} x {n} = {n*c}")
print("PROGRAMA ENCERRADO")
