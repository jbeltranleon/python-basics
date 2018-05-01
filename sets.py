""" Son como Conjuntos 
	
	Uno de los usos comunes con los sets es saber si un elemento pertenece a un set,
	si queremos saber si un elemento pertenece a una lista es mucho menos eficiente
	comparado con un set.
	Sí tenemos un gran número de elementos y sabemos que no se repiten ó no nos
	importa si se repiten es mucho mas eficiente realizar operaciones con sets que 
	con listas
"""

s = set([1,2,3])
t = set([3,4,5])

union = s.union(t)
print(union)

intersection = s.intersection(t)
print(intersection)

difference = s.difference(t)
print(difference)

# if 1 not in s:
if 1 in s:
	print('Pertenece')
else:
	print('No pertenece')