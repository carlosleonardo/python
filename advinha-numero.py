import random

print("Advinha o Número")
numero_secreto = random.randint(1, 10)
palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
if palpite == numero_secreto:
	print("Parabéns! Você acertou!")
elif palpite < numero_secreto:
	print("Muito baixo! Tente novamente.")
else:
	print("Muito alto! Tente novamente.")