print("Estatísticas de Notas")
while True:
    notas = []
    while True:
        nota = input("Digite a nota (ou '-1' para encerrar): ")
        if nota == "-1":
            break
        try:
            numero = float(nota)
            if 0 <= numero <= 10:
                notas.append(numero)
                # Calcula e exibe as estatísticas após cada entrada válida
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Por favor, digite uma nota válida.")
	
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média atual: {media}")
        print(f"Total de notas: {len(notas)}")
        print(f"Maior nota: {max(notas)}")
        print(f"Menor nota: {min(notas)}")
    else:
        print("Nenhuma nota foi digitada.")
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break