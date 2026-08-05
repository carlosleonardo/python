print("Índice de Massa Corporal (IMC)")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")  # Imprime o IMC com 2 casas decimais
