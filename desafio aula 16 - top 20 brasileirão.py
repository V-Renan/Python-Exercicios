times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athleico - PR',
         'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
         'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print('==='*20)
print(f"Listas de times do BRASILEIRÃO: {times}")
print('==='*20)
print(f"Os 5 primeiros são {times[0:6]}")
print('==='*20)
print(f"Os 4 últimos são {times[16:]}")#OU {times[-4:]}
print('==='*20)
print(f"Times em ordem alfabética: {sorted(times)}")
print('==='*20)
print(f"O Flamengo está na {times.index('Flamengo')+1}ª posição.")


