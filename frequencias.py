def calcular_frequencia_letras(texto):
	"""
	Calcula a frequência de cada letra em um texto.
	
	Args:
		texto (str): O texto para analisar
		
	Returns:
		dict: Dicionário com as letras como chaves e suas frequências como valores
	"""
	# Converter para minúsculas e manter apenas letras
	texto_limpo = ''.join(char.lower() for char in texto if char.isalpha())
	
	# Contar frequência de cada letra
	frequencias = {}
	for letra in texto_limpo:
		frequencias[letra] = frequencias.get(letra, 0) + 1
	
	return frequencias

def exibir_frequencias(frequencias):
	"""
	Exibe as frequências ordenadas por letra.
	
	Args:
		frequencias (dict): Dicionário com as frequências das letras
	"""
	print("Frequência das letras:")
	for letra in sorted(frequencias.keys()):
		print(f"{letra}: {frequencias[letra]}")

# Exemplo de uso
if __name__ == "__main__":
	texto = input("Digite o texto para análise: ")
	freq = calcular_frequencia_letras(texto)
	exibir_frequencias(freq)