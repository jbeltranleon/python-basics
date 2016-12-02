# -*- coding: utf-8 -*-



#If, seguido de tu condición, elif para anidar mas condiciones, 
#else nos ayuda a crear una condición por defecto en caso de no cumpla nada anterior:
import random

def importantDecision(destino):
    if destino % 2 == 0:
        print "Los astros se alinean a tu favor, la respuesta es si"
    elif destino == 1:
        print "¡Virgen del carmen, no lo hagas!"
    else:
        print "Esta opcion desafia las leyes de la logica, nunca saldrá"

importantDecision((random.randrange(10))+1)


#While

ipod_dibujo = ["╔═══╗ ♪", "║███║ ♫", "║ ● ║  ♫", "╚═══╝♪♪" ]

def dibujar(indice):
	contador = 0
	while contador < indice:
	    print ipod_dibujo[contador]
	    contador += 1

dibujar(4)


#For

notas = ["Fa", "Sol", "La", "Si", "Do", "Re", "Mi"]

# Uso un for para recorrer la lista e imprimir la funcion con todos los signos
for nota in notas:
    print nota
