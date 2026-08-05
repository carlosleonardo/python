import re
print("Validação de CPF")
cpf = input("Digite um CPF: ")
if len(cpf) != 14:
	print("CPF deve conter 14 caracteres (incluindo pontos e traço).")	
elif not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf):
	print("CPF deve conter apenas números.")
else:
	print("CPF válido.")
	