#try: Codigo que puede causar error
#except: manejo del error
#else: si no sucede un error
#finally: Se ejecuta siempre sin importar que suceda

countries = {
	'mexico': 122,
	'colombia': 49,
	'argentina': 43,
	'chile': 18,
	'peru': 31 
}

while True:
	country = str(input('Escribe el nombre de un pais: ')).lower()

	try:
		print('La población de {} es de: {} millones'.format(country, countries[country]))
	
	except KeyError:
		print('{} no está en nuestro diccionario'.format(country))