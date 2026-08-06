print("Encontrar o valor de 'o' substituindo 'a' em uma lista de strings")
frase =input("Digite uma frase: ").split()
# Substituindo 'a' por 'o' na frase
frase_modificada = [palavra.replace('a', 'o') for palavra in frase]
print("Frase modificada:", " ".join(frase_modificada))
