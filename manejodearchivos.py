import string
import random

creando_archivo = open("archivoCreadoConPython.txt","wb")
creando_archivo.write("Python es el mejor lenguaje.\nEs genial!!\n")
for i in range(1000):
    texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    creando_archivo.write("%s" % texto)
creando_archivo.close()

leyendo_archivo = open("archivoCreadoConPython.txt","r+")
leido = leyendo_archivo.read()
print leido
leyendo_archivo.close()