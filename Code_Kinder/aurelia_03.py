import turtle

colors=['blue', 'green']
t=turtle.Pen()
turtle.bgcolor('red')
for x in range(360):
    t.pencolor(colors[x%2])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

