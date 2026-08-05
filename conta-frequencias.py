from collections import Counter

def conta_frequencias(lista):
	frequencias = Counter(lista)
	return dict(frequencias)

# Exemplo de uso
itens = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
frequencias = conta_frequencias(itens)	
print(frequencias)
texto = "hello world"
frequencias_texto = conta_frequencias(texto)
print(frequencias_texto)