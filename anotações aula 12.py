cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "roxo": "\033[35m",
         "azul ciano": "\033[36m",
         "fAzul ciano": "\033[46m",
         "inverter": "\033[7m"}
nome = str(input("Qual o seu nome? ")).upper()
if nome == "VICTOR":
    print(f"Iai {cores['azul ciano']}{nome.capitalize()}{cores['limpa']}, que bom te por aqui ver novamente!!")
elif nome == "GIZELLE" or nome == "NILDA":
    print(f"Olá {cores['roxo']}{nome.capitalize()}{cores['limpa']}, eu te conheço em rs, tenha um ótimo dia!!")
else:
    print(f"Opa {cores['azul']}{nome.capitalize()}{cores['limpa']}, não sei quem é você mas adorarei te conhecer!! ")
