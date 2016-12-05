# -*- coding: utf-8 -*-
# Funciones comunes y utiles en python

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Nombre"
car1.color = "Rojo"
car1.value = 100000

# test code
print car1.description()