# preciso de um programa que leia o numero de uma op
# data ocorrido
# Nª equipamento
# Cor do artigo
# inutilizado
# Motivo
# Retrabalho
import datetime
insp = dict()
while True:
    insp['op'] = int(input("Digite o número da OP: "))
    print('Vamos adicionar a data? ')
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    insp['data'] = str(f'{dia}/{mes}/{ano}')
    insp['cor'] = str(input("Cor: "))
    insp['inutilizado'] = int(input("Inutilizado: "))
    insp['motivo'] = str(input("Motivo: "))
    insp['retrabalho'] = int(input("Retrablhado: "))
    while True:
        r = str(input("Quer adcionar mais uma op? [S/n] ")).upper()[0]
        if r in "SN":
            break
    if r == 'N':
        break
print(f"{'Número da OP':<5} {'Data do Ocorrido':>10} {'Cor':>10}")

