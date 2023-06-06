def lin():
    print('---' * 20)


def mensagem(msg):
    lin()
    print("     CONTROLE DE TERRENOS     ")
    lin()
    print(msg)
    lin()


def area(largura, comprimento):
    a = largura * comprimento
    mensagem(f"A aréa de  um terreno {l:.1f}x{c:.1f} é de {a}m²")


l = float(input("LARGURA: "))
c = float(input("COMPRIMENTO: "))
#area = largura * comprimento
area(l, c)

