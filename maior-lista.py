print("Digite 10 números para encontrar o maior:")
maior = None
for i in range(10):
	numero = int(input("Digite um número : "))
	if maior is None or numero > maior:
		maior = numero
print(f"O maior número digitado foi: {maior}")