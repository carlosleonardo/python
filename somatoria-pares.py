print("Soma todos os números pares de 1 a 100")
soma = sum(i for i in range(1, 101) if i % 2 == 0)
print(f"A soma dos números pares de 1 a 100 é: {soma}")