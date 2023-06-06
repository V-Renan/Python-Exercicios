from time import sleep
import emoji
from emoji import emojize
from datetime import date
ano = date.today().year
contagem = input(f"Vamos dar início a contagem regressiva paras os fogos da virada do ano de {ano}? ")
if contagem == 'sim':
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    print(emoji.emojize(':tada:', language='alias'))
else:
    print("Ok, quando chegar a hora, basta iniciar.")