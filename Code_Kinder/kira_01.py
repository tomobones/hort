import turtle

colors=[ 'cyan4','cyan2','green2']
t=turtle.Pen()
turtle.bgcolor('pink')
for x in range(333):
    t.pencolor(colors[x%3])
    t.width(22+44)
    t.forward(x)
    t.left(33)
turtle.Screen().exitonclick()

	
