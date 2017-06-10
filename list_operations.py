list_1 = [1]
list_2 = [2, 3, 4, 5]
list_sum = list_1 + list_2
print('Sumo lista 1 {} y lista 2 {} y como resultado tengo {}'.format(list_1, list_2, list_sum))

lista_3 = ['a']
list_mult = lista_3 * 3

print('\nLa lista {} es multiplicada por 3 y da : {}'.format(lista_3, list_mult))

list_sum.extend(list_mult)
print('\nSumo a la lista sum la lista mult {}'.format(list_sum))

secuence = [1,2,3,4,5,6,7,8,9]
del secuence[8]

secuence_reversed = secuence[::-1]
print('\nInvertimos la lista {}'.format(secuence_reversed))

secuence_reversed[0] = 3000

print('\nCambio el dato en el primer indice {}'.format(secuence_reversed))

valor = secuence_reversed.pop()
print('\nSacamos el último elemento de la lista y lo convertimos en un valor {}'.format(valor))

secuence_reversed.sort()
print('\nOrdeno la lista y queda: {}'.format(secuence_reversed))

text = 'Engurrupletadores'
list_text = list(text)

print('\nLa string {} se convierte en lista {}'.format(text, list_text))

list_to_string = ''.join(list_text)

print('De lista a string de nuevo {}'.format(list_to_string))
