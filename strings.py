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

def slices(text):
	print('\nEntramos a la función de rebanadas')
	print()
	ways = [text[1:]]
	print(ways)

if __name__ == '__main__':
	text = input('Ingresa una string: ')
	main(text)