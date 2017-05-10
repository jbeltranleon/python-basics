def factorial(number):
	if number == 0:
		return 1

	print(number)
	return number * factorial(number - 1)


if __name__ == '__main__':
	number = int(input('Set the number: '))

	result = factorial(number)

	print('Factorial of {} is {}'.format(number, result))