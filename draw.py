import turtle

def main():
	window = turtle.Screen()
	pencil = turtle.Turtle()
	
	make_square(pencil)

	turtle.mainloop()

def make_square(pencil):
	length = int(input('Tamaño: '))

	for i in range(4):
		make_line_and_turn(pencil, length)

def make_line_and_turn(pencil, length):
	pencil.forward(length)
	pencil.left(90)


if __name__ == '__main__':
	main()