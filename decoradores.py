print("Decoradores em Python")
def decorador(funcao):
	def wrapper(*args, **kwargs):
		print("Antes da execução da função.")
		resultado = funcao(*args, **kwargs)
		print("Depois da execução da função.")
		return resultado
	return wrapper

@decorador
def minha_funcao():
	print("Esta é a função decorada.")

minha_funcao()