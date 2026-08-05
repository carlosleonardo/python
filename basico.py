import math

lista = [1, 2, 3, 4, 5]
print(lista[-1])  # Acessar o último elemento
nomes = {1: "Alice", 2: "Bob", 3: "Charlie"}
conjunto = set(nomes.values())
conjunto2 = {"David", "Eve", "Frank"}
print(conjunto | conjunto2)  # União
print(conjunto & conjunto2)  # Interseção	
print(conjunto - conjunto2)  # Diferença
tupla1 = (1, 2, 3)
print(tupla1[0])  # Acessar o primeiro elemento
tupla2 = 4,5,6
print(tupla2)  # Imprime a tupla completa
print(tupla1 + tupla2)  # Concatenação de tuplas
print(len(tupla1))  # Tamanho da tupla
print(2 in tupla1)  # Verificar se um elemento está na tupla
print(tupla1[:-2])  # Fatiamento da tupla
a,b,c = tupla1  # Desempacotamento de tupla
print(a, b, c)  # Imprime os valores desempacotados
nome = "Alice"
t = nome*3
print(t)  # Imprime "AliceAliceAlice"
x = 5
y = 10
c = x // y  # Divisão inteira
print(c)  # Imprime 0
d = x % y  # Resto da divisão
print(d)  # Imprime 5
angulo = 30
radianos = math.radians(angulo)  # Converter para radianos
print(radianos)  # Imprime o valor em radianos
seno = math.sin(radianos)  # Calcular o seno
print(seno)  # Imprime o valor do seno
valor = 16
print(str(valor), type(str(valor)))  # Converte o número para string
print(int("42"), type(int("42")))  # Converte a string para inteiro
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")  # Imprime uma saudação personalizada
print("Olá, de novo, {}".format(nome))  # Outra forma de formatar a string
print("Olá, " + nome)  # Concatenando strings
print("Texto na mesma linha", end=" ")  # Imprime sem quebrar a linha
print("continuação do texto")  # Imprime na mesma linha