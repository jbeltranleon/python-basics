def protected(func):
	def wrapper(password):
		if password == 'platzi':
			return func()
		else:
			print('Contraseña erronea')

	return wrapper

@protected
def protected_func():
	print('Tú contraseña es correcta')


if __name__ == '__main__':
	password = str(input('Ingresa tu contraseña: '))
	
	protected_func(password)