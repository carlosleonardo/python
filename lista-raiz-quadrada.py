print("Raiz quadrada usando uma lista")

# Criando uma lista para armazenar os resultados
raizes = []
# Calculando a raiz quadrada de números pares entre 0 a 20 e armazenando na lista
for i in range(21):
	raizes = [i**0.5 if i % 2 == 0 else None for i in range(21)]
print("Raízes quadradas de números pares entre 0 e 20:")
for i in range(21):
	if raizes[i] is not None:
		print(f"A raiz quadrada de {i} é {raizes[i]:.2f}")