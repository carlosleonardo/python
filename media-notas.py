print("Cálculo da média de notas")
def calcular_media(notas):
	if not notas:
		return 0
	return sum(notas) / len(notas)

print("Informe as notas separadas por vírgula:")
entrada = input()
notas = [float(nota) for nota in entrada.split(",")]
media = calcular_media(notas)
print(f"A média das notas é: {media:.2f}")
if media >= 6:
	print("Aprovado")
elif media == 10:
	print("Aprovado com distinção")
else:
	print("Reprovado")