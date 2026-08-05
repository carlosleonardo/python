print("Números divisíveis por 3 ou 5 entre 0 e 30 usando uma lista")
numeros = [i for i in range(31) if i % 3 == 0 or i % 5 == 0]
print("Números divisíveis por 3 ou 5 entre 0 e 30:", numeros)