print("Queda Livre")
altura = float(input("Digite a altura inicial (em metros): "))
gravidade = 9.8
tempo = (2 * altura / gravidade) ** 0.5
print(f"O tempo de queda livre é: {tempo:.2f} segundos")