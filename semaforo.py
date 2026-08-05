print("Semáforo")
cor = input("Digite a cor do semáforo (vermelho, amarelo, verde): ").lower()
match cor:	
	case "vermelho":
		print("Pare!")
	case "amarelo":
		print("Atenção!")
	case "verde":
		print("Siga!")
	case _:
		print("Cor inválida. Por favor, digite vermelho, amarelo ou verde.")