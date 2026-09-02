import re

while True:
    print("Frequência de Palavras")
    texto = input("Digite um texto: ")
    palavras = re.findall(r'\b\w+\b', texto)
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    for palavra, contagem in frequencia.items():
        print(f"{palavra}: {contagem}")
    print()
    continuar = input("Deseja digitar outro texto? (s/n): ")
    if continuar.lower() != 's':
        break
