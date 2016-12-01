import datetime
from dateutil.relativedelta import relativedelta

fecha = datetime.date.today()
justoAhora = datetime.datetime.now()

print fecha
print justoAhora

# Nos podemos ayudar para concer los metodos con dir
print dir(datetime.date)

print justoAhora.weekday()
print justoAhora.day
print justoAhora.year

# Relative Time Delta

# De Hoy en 6 meses
print "La fecha de hoy en seis meses es %s" % (fecha + relativedelta(months=+6))
print "La fecha de hoy en seis dias es %s" % (fecha + relativedelta(days=+6))


#Cuando se selecciona una fecha desde por ejemplo JS
texto_fecha = "February 20 1997 12:30am GMT-5"

# Quitamos los caracteres de la zona horaria
texto_fecha = texto_fecha[:-5]

#Definimos el formato para la fecha
formatting = "%B %d %Y %I:%M%p "

#Convertimos el texto de la fecha a formato fecha
print datetime.datetime.strptime(texto_fecha, formatting)






