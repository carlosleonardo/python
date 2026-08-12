print("Imprime múltiplos de um número")
numero = int(input("Digite o número: "))
limite = int(input("Digite o limite: "))
for i in range(1, limite + 1):
    if i % numero == 0:
        print(i)
		