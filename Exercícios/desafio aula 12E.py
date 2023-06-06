v1 = float(input("Primeira nota: "))
v2 = float(input("Segunda nota: "))
media = (v1 + v2) / 2
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'limpa': '\033[m'}
if media < 5:
    print(f"Sua média é {cores['vermelho']}{media:.1f}{cores['limpa']}, você foi {cores['vermelho']}reprovado.{cores['limpa']}")
elif 7 > media >= 5:
    print(f"Sua média é {cores['amarelo']}{media:.1f}{cores['limpa']}, você está de {cores['amarelo']}recuperação.{cores['limpa']}")
elif media >= 7:
    print(f"Sua média é {cores['azul']}{media:.1f}{cores['limpa']}, parabéns você foi {cores['azul']}APROVADO{cores['limpa']}!!")
# Deste modo ---7 > media >= 5: é mais clean e siginifica q a média do aluno está entre 7 e 5.