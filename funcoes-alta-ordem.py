print("Funções de alta ordem em Python")
def aplicar_operacao(operacao, a, b):
	return operacao(a, b)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Multiplicação")
opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
	resultado = aplicar_operacao(lambda x, y: x + y, num1, num2)
elif opcao == "2":
	resultado = aplicar_operacao(lambda x, y: x * y, num1, num2)
else:
	resultado = "Opção inválida"

print(f"Resultado: {resultado}")

