import random
print("Rolagem de Dados Iniciada")
frequencias = [0] * 6
num_rolls = 6000000
for _ in range(num_rolls):
	roll = random.randint(1, 6)
	frequencias[roll - 1] += 1
print("Face\tFrequência\tPorcentagem")
for face in range(1, 7):
	porcentagem = (frequencias[face - 1] / num_rolls) * 100
	print(f"{face}\t{frequencias[face - 1]}\t\t{porcentagem:.2f}%")