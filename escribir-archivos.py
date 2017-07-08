#With es un manejador de contexto que se usa cuando ciertas operaciones van en par
#Como abrir y luego tener que cerrar un archivo
def run():
	with open('numeros.txt', 'w') as f:
		for i  in range(10):
			f.write(str(i))


if __name__ == '__main__':
	run()