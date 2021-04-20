import  turtle

colors = ['purple', 'red', 'blue', 'gray', 'yellow', 'orange']

t=turtle.Pen()
turtle.bgcolor('black')
for x in range(400):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(60)
