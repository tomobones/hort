import turtle

colors=['black', 'purple']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
   t.pencolor(colors[x%2])
   t.width(x/100+1)
   t.forward(x)
   t.left(45)

