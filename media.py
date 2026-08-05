print("Calcular a média de uma lista de números")
def calcular_media(numeros):
	if not numeros:
		return 0
	return sum(numeros) / len(numeros)

print("Informe uma lista de números separados por vírgula:")
entrada = input()
lista_numeros = [float(num.strip()) for num in entrada.split(",")]
media = calcular_media(lista_numeros)
print(f"A média dos números informados é: {media:.2f}")