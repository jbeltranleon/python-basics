from colorama import init, Fore, Back, Style

init()

def main(text):
	print(Fore.MAGENTA+'\nEl string que ingresaste es: {}'.format(text))

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
	change_word(text)
	compare(text)

def slices(text):
	print(Fore.RED+'\nEntramos a la función de rebanadas')
	print()
	ways = [text[1:], text[1:5], text[1:5:2], text[::-1]]
	print(ways)
	print('Para la ultima es de donde a donde y de cuanto en cuanto')

def palindrome(text):
	print(Fore.CYAN+'\nVamos a averiguar si la palabra es un palindromo')
	without_spaces_text = text.replace(' ', '')

	if without_spaces_text == without_spaces_text[::-1]:
		print('La cadena {} SI es un palindromo'.format(text))
	else:
		print('La cadena {} no es un palindromo'.format(text))

def change_word(text):
	new_string = 'L' + text[1:]
	print(Fore.GREEN+'\nLa nueva string es: {}'.format(new_string))

def compare(text):
	if text == 'jhonbeltran.com':
		print(Fore.YELLOW+'\n¡Esa es mi página web!')
	elif text > 'z':
		print(Fore.YELLOW+'\nLa letra {} es mayor que la <<a>>'.format(text[0]))
	else:
		print(Fore.YELLOW+'\nLa cadena ha pasado por la función compare(text)')

if __name__ == '__main__':
	text = input('Ingresa una string: ')
	main(text)