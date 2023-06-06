"""teste = list()
teste.append('Victor')
teste.append(23)
galera = list()
galera.append(teste[:])
teste[0] = 'João'
teste[1] = 27
galera.append(teste[:])
print(galera)"""





'''galera = [['João', 27, 'Masculino'], ['Victor', 23, 'Masculino'], ['Gizelle', 22, 'Feminino'], ['Nilda', 40, 'Feminino']]
print('--' * 21)
print(f"""{'MENU':^40}
[1] Para ver os dados da primeira pessoa.
[2] Para ver os dados da segunda pessoa.
[3] Para ver os dados da terceira pessoa.
[4] Para ver os dados da quarta pessoa.""")
print('--' * 21)
op = int(input("Sua opção: "))
if op == 1:
    print(f"Nome: {galera[0][0]} \nIdade: {galera[0][1]} anos \nSexo: {galera[0][2]}")
elif op == 2:
    print(f"Nome: {galera[1][0]} \nIdade: {galera[1][1]} anos \nSexo: {galera[1][2]}")
elif op == 3:
    print(f"Nome: {galera[2][0]} \nIdade: {galera[2][1]} anos \nSexo: {galera[2][2]}")
elif op == 4:
    print(f"Nome: {galera[3][0]} \nIdade: {galera[3][1]} anos \nSexo: {galera[3][2]}")
else:
    print("Opção inválida!")'''




"""galera = [['João', 27, 'Masculino'], ['Victor', 23, 'Masculino'], ['Gizelle', 22, 'Feminino'], ['Nilda', 40, 'Feminino']]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos e é do sexo {p[2]}")"""



galera = list()
dados = list()
menor = maior = 0
for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    dados.append(str(input("Sexo: ")))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        menor += 1
print(f"Temos {maior} maiores e {menor} menores de idade.")
