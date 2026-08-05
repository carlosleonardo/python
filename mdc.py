def mdc(a, b):
	while b:
		a, b = b, a % b
	return a

# Exemplo de uso
print("Calcular o Máximo Divisor Comum (MDC) de dois números")
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
resultado = mdc(num1, num2)
print(f"O MDC de {num1} e {num2} é {resultado}")

