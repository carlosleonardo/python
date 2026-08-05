print("Número Divisível")
numero = int(input("Digite um número: "))
divisor = int(input("Digite o divisor: "))
if numero % divisor == 0:
    print(f"O número {numero} é divisível por {divisor}.")
else:
    print(f"O número {numero} não é divisível por {divisor}.")