calificaciones = {}
calificaciones['algoritmos'] = 5
calificaciones['matematicas'] = 5
calificaciones['ingles'] = 4
calificaciones['finanzas'] = 3

for key in calificaciones:
	print(key)

suma_de_calificaciones = 0
for calificacion in calificaciones.values():
	suma_de_calificaciones += calificacion

print(suma_de_calificaciones)
promedio = suma_de_calificaciones / len(calificaciones.values())
print(promedio)

for key, value in calificaciones.items():
	print('llave: {} : valor: {}'.format(key, value))