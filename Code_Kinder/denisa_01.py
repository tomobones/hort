import turtle

colors = [ 'aquamarine', 'medium violet red', 'turquoise1', 'PaleGreen1', 'yellow', 'indian red']

t=turtle.Pen()
turtle.bgcolor('maroon2')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/10000000000000+10)
    t.forward(x)
    t.left(91)
turtle.Screen().exitonclick()
