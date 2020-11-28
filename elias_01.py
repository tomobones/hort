import turtle
stift=turtle.Pen()
turtle.bgcolor('black')
stift.width(5)

stift.pencolor('blue')

stift.forward(100)
stift.left(90)

stift.pencolor('green')
stift.forward(100)
stift.left(90)

stift.pencolor('yellow')
stift.forward(100)
stift.left(90)

stift.pencolor('brown')
stift.forward(110)
stift.left(90)

stift.pencolor('purple')
stift.forward(110)
stift.left(90)

stift.pencolor('orange')
stift.forward(120)
stift.left(90)

stift.pencolor('red')
stift.forward(120)
stift.left(90)

for wert in range(1,100):
	stift.forward(100+wert)
	stift.left(20+wert)
        stift.pencolor('green')
        stift.forward(100+wert)
        stift.left(20+wert)
        stift.pencolor('blue')
	stift.forward(100+wert)
        stift.left(20+wert)
	stift.pencolor('purple')
        stift.forward(100+wert)
        stift.left(20+wert)

turtle.Screen().exitonclick()
