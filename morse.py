morse_code_dict = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	'Y': '-.--', 'Z': '--..'}
def text_to_morse(text):
	morse_text = ''
	for char in text.upper():
		if char in morse_code_dict:
			morse_text += morse_code_dict[char] + ' '
		elif char == ' ':
			morse_text += '/ '
	return morse_text.strip()


def morse_to_text(morse):
	text = ''
	words = morse.split(' / ')
	for word in words:
		letters = word.split()
		for letter in letters:
			for key, value in morse_code_dict.items():
				if value == letter:
					text += key
					break
		text += ' '
	return text.strip()

# Exibe um menu para codificar ou decodificar
while True:
	print("Código Morse Menu")
	print("1. Codificar Texto para Código Morse")
	print("2. Decodificar Código Morse para Texto")
	print("0. Sair")
	choice = input("Digite a opção desejada: ")
	match choice:
		case '1':
				user_text = input("Digite o texto para codificar: ")
				encoded = text_to_morse(user_text)
				print("Código Morse:", encoded)
		case '2':
				user_morse = input("Digite o código Morse para decodificar: ")
				decoded = morse_to_text(user_morse)
				print("Texto Decodificado:", decoded)
		case '0':
				print("Saindo...")
				break
		case _:
			print("Opção inválida.")
