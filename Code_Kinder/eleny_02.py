import turtle
stift = turtle.Pen()
farben = ['violet'purple'red']
turtle.bgcolor('black')
stift.pencolor('white')
for affe in range(100):
	stift.pencolor(farben[affe%3])
	stift.forward(affe)
	stift.left(99)
turtle.Screen().exitonclick()
