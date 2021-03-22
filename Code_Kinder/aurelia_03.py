import turtle

colors=['turquoise4', 'turquoise3']
t=turtle.Pen()
turtle.bgcolor('turquoise1')
for x in range(360):
    t.pencolor(colors[x%2])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

