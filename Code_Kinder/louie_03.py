import turtle

colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    t.left(10)
    t.left(1)
    t.left(10)
