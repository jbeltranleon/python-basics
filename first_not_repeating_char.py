"""
"abacabad" c
"abacabaabacaba" _
"""
def first_not_repeating_char(char_secuence):
	seen_letters = {}

	for i, letter in enumerate(char_secuence):
		if letter not in seen_letters:
			seen_letters[letter] = (i, 1)
		else:
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

	print(seen_letters)

	final_letters = []

	for key, value in seen_letters.items():
		if value[1] == 1:
			final_letters.append( (key, value[0]) )

	#La función lambda hace lo mismo que sort_order()
	# def sort_order(value):
	# 	return value[1]

	not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

	if not_repeated_letters:
		return not_repeated_letters[0][0]
	else:
		return '_'


if __name__ == '__main__':
	char_secuence = str(input('Escribe una secuencia de caracteres: '))

	result = first_not_repeating_char(char_secuence)

	if result == '_':
		print('Todos los caracteres se repiten')
	else:
		print('El primer caracater que no se repite es: {}'.format(result))