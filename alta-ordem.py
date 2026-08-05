print("Funções de alta ordem")
def transformar_lista(funcao, lista):
	lista_transformada = list(map(funcao, lista))
	return lista_transformada

def por_extenso(numero):
	extenso = {
		0: "zero",
		1: "um",
		2: "dois",
		3: "três",
		4: "quatro",
		5: "cinco",
		6: "seis",
		7: "sete",
		8: "oito",
		9: "nove"
	}
	return extenso.get(numero, str(numero))

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
por_extenso_numeros = transformar_lista(por_extenso, numeros)
print(por_extenso_numeros)