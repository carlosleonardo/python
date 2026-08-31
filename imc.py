print("Índice de Massa Corporal (IMC)")

while True:
	try:
		peso = float(input("Digite seu peso (kg): "))
		altura = float(input("Digite sua altura (m): "))
		imc = peso / (altura ** 2)
		print(f"Seu IMC é: {imc:.2f}")  # Imprime o IMC com 2 casas decimais
		if imc < 18.5:
			print("Você está abaixo do peso.")
		elif 18.5 <= imc < 24.9:
			print("Você está com o peso normal.")
		elif 25 <= imc < 29.9:
			print("Você está com sobrepeso.")
		else:
			print("Você está com obesidade.")

		continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
		
		if continuar != 's':
			break
	except ValueError:
		print("Por favor, insira um valor numérico válido.")
