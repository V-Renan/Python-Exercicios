'''import emoji
nome = str(input("Digite seu nome: ")).upper()
if nome == 'VICTOR':
    print(emoji.emojize(f"""Que surpresa, faz tempo que não te vejo por aqui!
Muito bom dia {nome.capitalize()} :relaxed:!!""", language="alias"))
else:
    print(emoji.emojize(f"Olá {nome.capitalize()}, não sei quem é você mas irei adorar te conhecer! :heart:", language="alias"))'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
print(f"A sua média foi {m:.1f}")
if m >=7.0:
    print("Parabéns você foi aprovado!!!")
else:
 print("Infelizmente você foi reprovado.")
