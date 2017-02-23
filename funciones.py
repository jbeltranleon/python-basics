# El cuerpo de una funcion se diferencia por la identacion que tiene 
#(4 espacios respecto a la declaracion de la funcion)

def saludar():
	return "Hola"

def despedir():
	print ("Chao")

print (saludar())
despedir()

# Funcion con parametros de entrada
def areaTriangulo(base, altura):
    resultado = (base*altura)/2
    return resultado

resultado = areaTriangulo(4.0,4)
print (resultado)


#Concatenando

def horoscopo(signo):
    return "Los astros se alinean a tu favor amigo %s" % signo


# Lista de signos
signos = ['Picis', 'Aries', 'Capricornio']

# Uso un for para recorrer la lista e imprimir la funcion con todos los signos
for signo in signos:
    print (horoscopo(signo))
    
