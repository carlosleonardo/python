import re

print("Extrair artigos de uma frase")
frase = input("Digite uma frase: ")
artigos = re.findall(r'\b(?:o|a|os|as|um|uma|uns|umas)\b', frase, re.IGNORECASE)
print(f"Os artigos da frase são: {artigos}")
# mostra a frase sem os artigos
frase_sem_artigos = re.sub(r'\b(?:o|a|os|as|um|uma|uns|umas)\b', '', frase, flags=re.IGNORECASE)
print(f"A frase sem os artigos é: {frase_sem_artigos.strip()}")