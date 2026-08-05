print("Progressão Aritmética")
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
n = int(input("Digite o número de termos: "))

for i in range(n):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")
print()