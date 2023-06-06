def voto(ano):
    from datetime import date # O datetime importado dentro da def economiza memoria
    atual = date.today().year
    idade = atual - ano
    print('--' * 20)
    if 18 < idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGÁTORIO. ')
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA. ')
    if idade > 65 or 16 <= idade < 18:
        return print(f'Com {idade} anos: VOTO OPICIONAL. ')


nascimento = int(input("Qual o ano de nascimento? "))
voto(nascimento)
