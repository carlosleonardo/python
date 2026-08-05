print("Extrair Artigos")
import re
texto = input("Digite um texto para extrair os artigos: ")
artigos = re.findall(r"\b(o|a|os|as)\b", texto, re.IGNORECASE)
if artigos:
	print("Artigos encontrados:", ", ".join(artigos))
else:
	print("Nenhum artigo encontrado.")
print("Texto sem os artigos:", re.sub(r"\b(o|a|os|as)\b", "", texto, flags=re.IGNORECASE).strip())