# -*- coding: utf-8 -*-
# Funciones comunes y utiles en python
import random
import time
from time import sleep

class BolaDeCristal(object):
    def __init__(self, nombre,destino):
        self.nombre = nombre
        self.destino = destino
    def saludar(self):
        return "Hola %s Sabia que vendrias a mi" % self.nombre
    def adivinar(self):
        if self.destino % 2 == 0:
            print "Los astros se alinean a su favor, la respuesta es si"
        elif self.destino % 2 != 0:
            print "¡Virgen del carmen, no debe hacerlo!"
        else:
            print "Vaia esto nunca va a aparecer!"


nombre = raw_input("¿Como te llamas?\n")
vaino = BolaDeCristal(nombre,random.randrange(1,10))

print vaino.saludar()
imput_no_hace_nada = raw_input("¿Que deseas preguntarle a los astros?\n")
print "¿Oh astros que debe hacer este mortal?\n"
sleep(2)

vaino.adivinar()