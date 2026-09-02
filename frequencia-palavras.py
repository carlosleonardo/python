from tokenizer import split_into_sentences

print("Contagem de Frequência de Palavras")
while True:
    texto = input("Digite um texto: ")
    palavras = split_into_sentences(texto)
    palavras = [palavra for frase in palavras for palavra in frase.split()]
    simbolos = set(".,!?;:()[]{}\"'")
    palavras = [palavra for palavra in palavras if palavra not in simbolos and palavra != '']
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