from time import sleep
c = ('\033[m',       # 0 - Sem cor
     '\033[0;30;41m',# 1 - Vermelho
     '\033[0;30;42m',# 2 - Verde
     '\033[0;30;43m',# 3 - Amarelo
     '\033[0;30;44m',# 4 - Azul
     '\033[0;30;45m',# 5 - Roxo
     '\033;[7;30m')  # 6 - Branco


def ajuda(com):
    titulo(f"ACESSANDO O MANUAL DO COMANDO \'{com}\'", 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f"  {msg}")
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblicoteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)
