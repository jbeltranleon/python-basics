# -*- coding: utf-8 -*-
# Funciones comunes y utiles en python

palabra = "Electroencefalografista"

print "La longitud de la palabra %s" % len(palabra)
print "El tipo de dato de la palabra es: %s" % type(palabra)

print range(0, 212,2)

print "NOTAS USANDO sum()"
primero = 2.9 * 0.24
segundo = 2.7 * 0.24
tercero = 3 * 0.32
auto = 4 * 0.10
coe = 3.33333 * 0.10

nota = sum([primero, segundo, tercero, auto, coe])
print "Su nota final es de: %s" % nota
print "Su nota con un solo decimal es: %s " % round(nota,1)

print map(str,[5,2,3])

print sorted([5,6,7,8,2,3,4,5,6,4,6,34,3,3,3,3,4,5,6,7,3])

print "Esto es todo lo que puedo hacer con una lista: %s" % dir([5,6,7,3])
print "________________________________________________________________"

print "Aiudaaa %s " % help(map) 

# Tipado tipo pato :v DuckType
print "Hola Tarola " * 12


#Para saber si algo está en una string
frase = "En la sintetica de las palmas"

print "sintetica" in frase


