#Listas y diccionarios con una sintaxis más natural

pair = []
for num in range(1, 31):
	if num % 2 == 0:
		pair.append(num)

print('Pares usando estructuras ya conocidas:\n{}'.format(pair))

pair_list_compr = [num for num in range(1, 31) if num % 2 == 0]

print('Pares usando List Comprehension:\n{}'.format(pair_list_compr))


squares = {}

for num in range(1, 11):
	squares[num] = num**2

print('Diccionario con el numero como llave y como valor el mismo numero al cuadrado')
print(squares)

squares_dict_compr = {num: num**2 for num in range(1, 11)}
print('Ahora usamos un Dictionary Comprehension')
print(squares_dict_compr)