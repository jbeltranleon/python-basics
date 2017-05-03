import turtle

window = turtle.Screen()
lapiz = turtle.Turtle()

for i in range(2**2):
	lapiz.forward(101//2)
	lapiz.left(90)

turtle.mainloop()