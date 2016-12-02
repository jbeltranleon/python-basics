# Factorial

def factorial(numero):
    acumulador = 1
    while numero > 0:
        acumulador = acumulador * numero
        numero = numero - 1

    print "El factorial es: %i" % acumulador

factorial(5)


# 5! = 5 * 4!
# 4! = 4 * 3!
# ...
# 2! = 2 * 1!
# 1! = 1 * 0 = 0 
def factorialRecursivo(numero):
    if numero == 0:
        return 1
    else: 
        return numero * factorialRecursivo(numero - 1)

print "Esto se hace mediante una funcion recursiva wooow %s" % factorialRecursivo(5)
