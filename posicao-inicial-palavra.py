import re

print("Mostra a posição de cada palavra")
frase = input("Digite uma frase: ")
palavras = re.findall(r'\b\w+\b', frase)
for palavra in palavras:
    posicao = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posição {posicao}")