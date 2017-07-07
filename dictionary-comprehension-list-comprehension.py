#Listas y diccionarios con una sintaxis más natural

pair = []
for num in range(1, 31):
	if num % 2 == 0:
		pair.append(num)

print('Pares usando estructuras ya conocidas:\n{}'.format(pair))

pair_list_compr = [num for num in range(1, 31) if num % 2 == 0]

print('Pares usando List Comprehension:\n{}'.format(pair_list_compr))