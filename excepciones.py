#!/usr/bin/env python
# -*-coding:utf-8-*-

# Para cualquier excepcion
try:
    r = 3 / 0
except:
    print "División entre 0"


# Para la division de 0
try:
    r = 3 / 0
except ZeroDivisionError:
    print "División entre 0"


# Excepcion por defecto
try:
    r = 3 / 0
except Exception as e:
    print "%s" % e

# Usamos pass para que nos permita continuar
try:
    r = 3 / 0
except Exception as e:
    pass

print "Esto aparece despues de usar pass"

# Tambien podemos mostrar un log de la excepcion
try:
    r = 3 / 0
except Exception as e:
    print "%s" % e
    raise e
