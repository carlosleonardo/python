print("Emoções")
emocao = input("Digite uma emoção (felicidade, tristeza, raiva, medo): ").lower()
match emocao:
	case "felicidade":
		print(":)")
	case "tristeza":
		print(":(")
	case "raiva":	
		print(":|")
	case "medo":
		print(":O")	
	case _:
		print("Emoção desconhecida")