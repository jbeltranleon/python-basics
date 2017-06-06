def main(text):
	print(text)

	methods = [ text.upper(),
				text.isupper(),
				text.lower(), 
				text.islower(), 
				text.find('a'), 
				text.isdigit(), 
				text.endswith('n'), 
				text.startswith('J'), 
				text.split('\n'), 
				text.join('||||||')]

	print(methods)

	slices(text)
	palindrome(text)

def slices(text):
	print('\nEntramos a la función de rebanadas')
	print()
	ways = [text[1:], text[1:5], text[1:5:2], text[::-1]]
	print(ways)
	print('Para la ultima es de donde a donde y de cuanto en cuanto')

def palindrome(text):
	print('\nVamos a averiguar si la palabra es un palindromo')
	without_spaces_text = text.replace(' ', '')

	if without_spaces_text == without_spaces_text[::-1]:
		print('La cadena {} SI es un palindromo'.format(text))
	else:
		print('La cadena {} no es un palindromo'.format(text))

if __name__ == '__main__':
	text = input('Ingresa una string: ')
	main(text)