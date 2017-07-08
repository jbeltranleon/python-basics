def run(word):
	counter = 0
	with open('el-arbol-de-diana-alejandra-pizarnik.txt', 'r') as f:
		#cada renglon es un string en una lista
		#print(f.readlines())
		for line in f:
			counter += line.count(word)

	print('La palabra {} se encuentra {} en el texto'.format(word, counter))

if __name__ == '__main__':
	word = str(input('Escribe una palabra para saber cuantas veces está en el texto: '))
	run(word)