pessoas = dict()
lista = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    while True:
        pessoas['sexo'] = str(input("Sexo: ")).upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print("Opção inválida, rsponda a apenas com [S / N].")
    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        r = str(input("Quer continuar? [S/N] ")).upper()[0]
        if r in 'SN':
            break
        print("Responda apenas com S ou N.")
    if r == 'N':
        break
print('-=-' * 20)
print(f"Ao todo temos {len(lista)} pessoas cadastradas. ")
media = soma / len(lista)
print(f"A média de idade é de {media:5.2f} anos.")
print(f"As mulheres cadastradas foram ", end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print("Lista das pessoas que estão acima da média:" )
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print('<< ENCERRADO >>')
