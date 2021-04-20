import turtle

colors=[ 'purple1', 'blue', 'cyan2', 'gold', 'green2']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(213):
    t.pencolor(colors[x%5])
    t.width(x/333+5)
    t.forward(x)
    t.left(59)
turtle.Screen().exitonclick()

