import math

print("Exemplo de funções em Python")

def saudacao(nome):
	return f"Olá, {nome}! Bem-vindo ao mundo da programação em Python."
def soma(a, b):
	return a + b

def acumular_soma(*numeros): # Permite somar uma quantidade variável de números
	total = 0
	for numero in numeros:
		total += numero
	return total

def operacoes_matematicas(a, b):
	soma = a + b
	subtracao = a - b
	multiplicacao = a * b
	divisao = a / b if b != 0 else "Divisão por zero não é permitida"
	return soma, subtracao, multiplicacao, divisao

print("Função de saudação:")
nome_usuario = input("Digite seu nome: ")
print(saudacao(nome_usuario))
print("\nFunção de soma:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = soma(num1, num2)
print(f"A soma de {num1} e {num2} é: {resultado}")
print("Fatorial de um número:")
num = int(input("Digite um número: "))
print(f"O fatorial de {num} é: {math.factorial(num)}")
print("\nFunção de soma acumulada:")
numeros_para_somar = input("Digite números para somar (separados por espaço): ")
formatados = numeros_para_somar.split()
soma = acumular_soma(*map(float, formatados))
print(f"A soma acumulada dos números é: {soma}")
print("\nFunção de operações matemáticas:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma, subtracao, multiplicacao, divisao = operacoes_matematicas(num1, num2)
print(f"Soma: {soma}")	
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

print("\nFunção lambda para calcular o quadrado de um número:")
quadrado = lambda x: x ** 2
num = float(input("Digite um número: "))
print(f"O quadrado de {num} é: {quadrado(num)}")