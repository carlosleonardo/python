print("Contagem de vogais e consoantes")
texto = input("Digite um texto: ").lower()
vogais = "aeiouáéíóúâêô"
contagem_vogais = sum(1 for letra in texto if letra in vogais)
contagem_consoantes = sum(1 for letra in texto if letra.isalpha() and letra not in vogais)
print(f"Vogais: {contagem_vogais}")
print(f"Consoantes: {contagem_consoantes}")