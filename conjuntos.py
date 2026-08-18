print("Exemplo de conjuntos")	
a={1, 2, 3, 4, 5}
b={4, 5, 6, 7, 8}
print("Conjunto A:", a)
print("Conjunto B:", b)
# União
uniao = a.union(b)
print("União de A e B:", uniao)
# Interseção
intersecao = a.intersection(b)
print("Interseção de A e B:", intersecao)
# Diferença
diferenca = a.difference(b)
print("Diferença de A e B (A - B):", diferenca)
# Diferença simétrica
diferenca_simetrica = a.symmetric_difference(b)
print("Diferença simétrica de A e B:", diferenca_simetrica)