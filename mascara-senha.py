import re

print("Máscara de Senha")
senha = input("Digite uma senha: ")
if len(senha) < 8:
	print("A senha deve conter pelo menos 8 caracteres.")
elif not re.search(r"[A-Z]", senha):
	print("A senha deve conter pelo menos uma letra maiúscula.")
elif not re.search(r"[a-z]", senha):
	print("A senha deve conter pelo menos uma letra minúscula.")
elif not re.search(r"[0-9]", senha):
	print("A senha deve conter pelo menos um número.")
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
	print("A senha deve conter pelo menos um caractere especial.")
else:
	print("Senha válida.")