import turtle 
t = turtle.Pen()
for x in range(100):
	t.forward(x)
	t.left(90)
	t.pencolor('blue')
	t.forward(100)
	t.left(50)
turtle.Screen().exitionclick()
