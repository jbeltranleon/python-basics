#If, seguido de tu condición, elif para anidar mas condiciones,
#else nos ayuda a crear una condición por defecto en caso de no cumpla nada anterior:
import random
from colorama import init, Fore

init()
def importantDecision(destino):
    if destino % 2 == 0:
        print ("Los astros se alinean a tu favor, la respuesta es si")
    elif destino % 2 != 0:
        print ("¡Virgen del carmen, no lo hagas!")
    else:
        print ("Vaia esto nunca va a aparecer!")

importantDecision((random.randrange(10))+1)


#While

ipod_dibujo = ["╔═══╗ ♪", "║███║ ♫", "║ ● ║  ♫", "╚═══╝♪♪" ]

def dibujar(indice):
	contador = 0
	while contador < indice:
	    print (ipod_dibujo[contador])
	    contador += 1

dibujar(4)


#For

notas = ["Fa", "Sol", "La", "Si", "Do", "Re", "Mi"]

# Uso un for para recorrer la lista e imprimir la funcion con todas las notas
for nota in notas:
    print (Fore.RED+nota)

#For con rangos
for i in range(0, 16,3):
	print (Fore.CYAN+"Numero {}".format(i))

for i in "Spelling":
	print (Fore.RED+"%s" % i)


print(Fore.CYAN+'Vamos a elevar al cuadrado solamente a los numeros divisibles por 3')
for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)

print(Fore.WHITE+'Usando el break')
for i in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        break
