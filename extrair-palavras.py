import re

print("Extrator palavras de uma frase")
frase = input("Digite uma frase: ")
palavras = re.findall(r'\b\w+\b', frase)
print(f"As palavras da frase são: {palavras}")