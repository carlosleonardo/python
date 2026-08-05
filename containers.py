numeros = [1,2,3,4,5]
print("Lista de números:", numeros)
print("Tipo da variável 'numeros':", type(numeros))
quadrado_pares = [(x, x**2) for x in numeros if x % 2 == 0]
print("Quadrados dos números pares:", quadrado_pares)