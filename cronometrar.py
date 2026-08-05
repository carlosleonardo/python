print("Cronometrar o tempo de execução de um código")

import time

def cronometrar(funcao):
	def wrapper(*args, **kwargs):
		inicio = time.time()
		resultado = funcao(*args, **kwargs)
		fim = time.time()
		print(f"Tempo de execução: {fim - inicio:.4f} segundos")
		return resultado
	return wrapper

@cronometrar
def exemplo_funcao():
	soma = 0
	for i in range(1, 1000000):
		soma += i
	return soma

exemplo_funcao()