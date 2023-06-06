import random
palpite = 1
print('\033[35m-=-\033[m' * 22)
n = random.randint(0, 10)
print(n)
print("\033[36mCOMPUTADOR>>> Vou pensar em número de 0 a 10, consegue advinhar?\033[m ")
print('\033[35m-=-\033[m' * 22)
jogador = int(input("Faça seu chute: "))
while n != jogador:
    palpite += 1
    jogador = int(input("""\033[31mERROU, tente novamente.\033[m
>> """))
if n == jogador:
    print(f"\033[34mParabéns, você acertou em {palpite} palpites.!!!")
