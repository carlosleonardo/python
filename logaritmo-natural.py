print("Logaritmo Natural")
import math
numero = float(input("Digite um número para calcular o logaritmo natural: "))
if numero > 0:
	logaritmo = math.log(numero)
	print(f"O logaritmo natural de {numero} é: {logaritmo:.4f}")
else:
	print("O número deve ser maior que zero para calcular o logaritmo natural.")
