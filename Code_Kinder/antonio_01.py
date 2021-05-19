import  turtle

colors = ['red', 'blue']

t=turtle.Pen()
turtle.bgcolor('black')
for x in range(400):
    t.pencolor(colors[x%2])
    t.width(x/100+1)
    t.forward(x)
    t.left(90)

turtle.Screen().exitonclick()
