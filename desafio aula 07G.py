larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {} de tinta.'.format(larg, alt, área, área/2))
