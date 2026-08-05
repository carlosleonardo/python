for numero in range(1, 101):
	raiz = int(numero ** 0.5)
	if raiz * raiz == numero:
		print(f"{numero} é um quadrado perfeito.")