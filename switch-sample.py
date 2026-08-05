linguagem = input("Escolha a linguagem (Python, Java, C++): ")
match linguagem:
	case "Python":
		print("Você escolheu Python!")
	case "Java":
		print("Você escolheu Java!")
	case "C++":
		print("Você escolheu C++!")
	case _:
		print("Linguagem não reconhecida.")
		
