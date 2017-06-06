import random

def main():
	number_found = False
	size = int(input('Hasta que numero deseas rifar?\n'))
	random_number = random.randint(0, size)

	while not number_found:
		number = int(input('Escoge un número: \n'))

		if number == random_number:
			print('Encontraste el número {}'.format(random_number))
			number_found = True

if __name__ == '__main__':
	main()