nome = str(input("Digite seu nome: ")).capitalize()
hora_Atual = int(input("Que horas são? "))
if (hora_Atual >= 0 and hora_Atual < 12):
    mensagem = "Bom dia!"
elif (hora_Atual >= 12 and hora_Atual < 18):
    mensagem = "Boa tarde!"
elif (hora_Atual >= 18 and hora_Atual <= 24):
    mensagem = "Boa noite!"

print(mensagem, nome)


for cont in range(10):
    print( cont)