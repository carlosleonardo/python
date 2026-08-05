import math

num = int(input("Digite um ângulo em graus: "))
radianos = math.radians(num)  # Converter para radianos
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")