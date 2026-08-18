print("Utilizando semáforos para controlar o acesso a recursos compartilhados em Python.")

import threading

# Criando um semáforo com capacidade para 2 threads
semaforo = threading.Semaphore(2)

def tarefa(nome):
	print(f"{nome} está esperando para acessar o recurso.")
	with semaforo:
		print(f"{nome} está acessando o recurso.")
		# Simulando uma operação que leva tempo
		import time
		time.sleep(2)
		print(f"{nome} terminou de acessar o recurso.")

# Criando e iniciando threads
threads = []
for i in range(5):
	t = threading.Thread(target=tarefa, args=(f"Thread-{i+1}",))
	threads.append(t)
	t.start()

for t in threads:
	t.join()