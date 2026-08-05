print("Dicionário de alunos com notas usando uma lista de dicionários")
# Entrada de dados para o dicionário de alunos
alunos = []
while True:
	nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
	if nome.lower() == 'sair':
		break
	nota = float(input(f"Digite a nota de {nome}: "))
	alunos.append({'nome': nome, 'nota': nota})

# Exibindo o dicionário de alunos usando dictionary comprehension
dicionario_alunos = {aluno['nome']: aluno['nota'] for aluno in alunos if aluno['nota'] >= 7}
print("Dicionário de alunos com notas >= 7:", dicionario_alunos)