import turtle

colors=['steel blue','azure2','deep pink']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%3])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.Screen().exitonclick()
