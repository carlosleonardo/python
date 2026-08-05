frase = input("Digite uma frase: ")
palavras = frase.split()
print("Palavras na frase:")
for palavra in palavras:
    count = palavras.count(palavra)
    print(f"{palavra} (aparece {count} vezes)")
