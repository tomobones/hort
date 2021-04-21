import  turtle
colors=['dark green','dark olive green','dark sea green']
t=turtle.Pen(10)
turtle.bgcolor('black')
for x in range(1000):
    t.pencolor(colors[x%3]) 
    t.width(x/5+5)
    t.forward(x)
    t.left(100)
turtle.Screen().exitonclick()
