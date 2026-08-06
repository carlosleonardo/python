print("Soma todos os números pares de 1 a 100")
try:
	total = int(input("Informe o total de números pares que deseja somar (1 a 100): "))
	if total < 1 or total > 100:
		raise ValueError("O número deve estar entre 1 e 100.")	
	
	numeros = []
	for i in range(1, total + 1):
		numero = int(input(f"Digite o {i}º número: "))
		numeros.append(numero)
	soma = sum(num for num in numeros if num % 2 == 0)
		
	print(f"A soma dos {total} primeiros números pares é: {soma}")
except ValueError as e:
	print(f"Erro: {e}")