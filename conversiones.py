# -*- coding: utf-8 -*-

def convertidometro(dato):
    if type(dato) == float:
        print "Ahora es un entero %s " % int(dato)
        print "Ahora es una cadena %s" % str(dato)
    elif type(dato) == int:
        print "Ahora es un número con coma flotante %s" % float(dato)
        print "Ahora es una cadena %s" % str(dato)
    elif type(dato) == str:
        print "Ahora es un número con coma flotante %s" % float(dato)
        print "Ahora es un entero %s" % int(float(dato))

print "--------Ingresando un float--------"
convertidometro(3.4)

print "--------Ingresando un int----------"
convertidometro(3)

print "--------Ingresando una str-------- "
convertidometro("3.0")

