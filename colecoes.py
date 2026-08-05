from collections import Counter

def contar_ocorrencias(lista):
	"""
	Conta as ocorrências de cada elemento em uma lista.

	Args:
		lista (list): A lista de elementos a ser contada.

	Returns:
		dict: Um dicionário com os elementos como chaves e suas ocorrências como valores.
	"""
	return dict(Counter(lista))

if __name__ == "__main__":
	# Exemplo de uso
	elementos = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
	ocorrencias = contar_ocorrencias(elementos)
	print("Ocorrências dos elementos:", ocorrencias)
	texto = "hello world"
	ocorrencias_texto = contar_ocorrencias(texto)
	print("Ocorrências dos caracteres no texto:", ocorrencias_texto)
	palavras = texto.split()
	ocorrencias_palavras = contar_ocorrencias(palavras)
	print("Ocorrências das palavras no texto:", ocorrencias_palavras)