# -*- coding: utf-8 -*-
# Funciones comunes y utiles en python
import random
import time
from time import sleep

class Dios(object):
    # def __init__(self, dios):
    #     self.dios = dios

    def bendecir(self):
        print "io te bendigo papu"

class BolaDeCristal(Dios):
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


# ala = Dios("Señor Alá")

nombre = raw_input("¿Como te llamas?\n")
vaino = BolaDeCristal(nombre,random.randrange(1,10))

print vaino.saludar()
imput_no_hace_nada = raw_input("¿Que deseas preguntarle a los astros?\n")
print "¿Oh astros que debe hacer este mortal?\n"
sleep(2)

vaino.adivinar()

bendicion = raw_input("¿Quieres que te bendiga?\n")
if bendicion == 'si':
    vaino.bendecir()
else:
    print "Entonces jodete"