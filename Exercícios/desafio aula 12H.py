peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f"Seu imc é {imc:.1f}, você está abaixo do seu peso ideal.")
# Método simplificado.
elif 18.5 <= imc < 25:
    print(f"Seu imc é {imc:.1f}, você está no seu peso ideal.")
elif imc >= 25 and imc < 30:
    print(f"Seu imc é {imc:.1f}, você está com sobrepeso.")
elif imc >= 30 and imc < 40:
    print(f"Seu imc é {imc:.1f}, você está com obesidade.")
elif imc >= 40:
    print(f"Seu imc é {imc:.1f}, você está com obesidade morbida.")