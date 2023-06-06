n = str(input("Digite seu nome: ")).strip()
nome = n.split()
print(f"""Olá {nome[1]}, prazer te conhecer!
Seu primeiro nome é {nome[0]}
Seu útimo nome é {nome[len(nome)-1]}""")
