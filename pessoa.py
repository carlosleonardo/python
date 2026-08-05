pessoas = {"Carlos":(51, "Marrom"), "Clara":(25, "Claro"), "Ana":(30, "Azul"), "João":(40, "Escuro")}
for nome, (idade, cor) in pessoas.items():
	print(f"{nome} tem {idade} anos e seus olhos são da cor {cor}.")
