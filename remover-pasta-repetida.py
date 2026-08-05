def remover_pasta_repetida(pastaRaiz, pastaRepetida):
	import os
	for root, dirs, files in os.walk(pastaRaiz):
		for dir in dirs:
			if dir == pastaRepetida:
				caminho_completo = os.path.join(root, dir)
				try:
					os.rmdir(caminho_completo)
					print(f"Pasta '{caminho_completo}' removida com sucesso.")
				except OSError as e:
					print(f"Erro ao remover a pasta '{caminho_completo}': {e}")

# Exemplo de uso:
pastaRaiz = input("Digite o caminho da pasta raiz: ")
pastaRepetida = input("Digite o nome da pasta repetida a ser removida: ")
remover_pasta_repetida(pastaRaiz, pastaRepetida)
	
	