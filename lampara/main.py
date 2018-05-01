from lamp import Lamp

def main():
	lamp = Lamp(is_turned_on = True)

	while True:
		command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))
		
		if command == 'p':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break	


if __name__ == '__main__':
	main()