from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
print('O ângulo de {} tem o SENO de: {:.2f} \nO ângulo de {} tem o COSSENO de: {:.2f} \nO ângulo de {} tem a TANGENTE de: {:.2f}'. format(ang, seno, ang, coss, ang, tan(radians(ang))))
