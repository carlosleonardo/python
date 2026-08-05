print("Aceleração de um objeto")
velocidade_inicial = float(input("Digite a velocidade inicial (m/s): "))
velocidade_final = float(input("Digite a velocidade final (m/s): "))
tempo = float(input("Digite o tempo (s): "))
aceleracao = (velocidade_final - velocidade_inicial) / tempo
print(f"A aceleração do objeto é: {aceleracao:.2f} m/s²")