def contagem_regressiva(n):
	if n < 0:
		print("Número deve ser não negativo.")
	elif n == 0:
		print("Contagem regressiva concluída!")
	else:
		print(n, end=' ')
		contagem_regressiva(n - 1)

print("Contagem regressiva")
numero = int(input("Digite um número para a contagem regressiva: "))
contagem_regressiva(numero)
