def fatorial(n):
	"""Calcula o fatorial de um número."""
	if n < 0:
		raise ValueError("Fatorial não é definido para números negativos")
	elif n == 0 or n == 1:
		return 1
	else:
		resultado = 1
		for i in range(2, n + 1):
			resultado *= i
		return resultado

# Exemplo de uso
if __name__ == "__main__":
	while True:
		try:
			numero = int(input("Digite um número ou -1 para sair: "))
			if numero == -1:
				break
			resultado = fatorial(numero)
			print(f"O fatorial de {numero} é {resultado}")
		except ValueError as e:
			print(f"Erro: {e}")
		
	