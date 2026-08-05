import re
from collections import Counter

print("Terminam com o ou a")
frase = input("Digite uma frase: ")
palavras = re.findall(r'\b\w+\b', frase)
conta_o = Counter(palavra.lower() for palavra in palavras if palavra.lower().endswith('o'))
conta_a = Counter(palavra.lower() for palavra in palavras if palavra.lower().endswith('a'))

# for palavra in palavras:
# 	if palavra.lower().endswith('o'):
# 		conta_o += 1
# 	elif palavra.lower().endswith('a'):
# 		conta_a += 1
print(f"Palavras que terminam com 'o': {sum(conta_o.values())}")
print(f"Palavras que terminam com 'a': {sum(conta_a.values())}")