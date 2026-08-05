def soma(*args):
	return sum(args)

print("Função de soma")
numeros = input("Digite números separados por espaço: ")
numeros_lista = list(map(float, numeros.split()))
resultado = soma(*numeros_lista)
print(f"A soma dos números é: {resultado}")