import turtle
import random

pen = turtle.Turtle()
colors = ["red", "red2", "red3", "red4", "tomato", "tomato2", "tomato3", "tomato4"]
  
def kurve(größe):
    for i in range(200):
        pen.right(1)
        pen.forward(.1 * größe)
  
def herz(x, y, größe, color):
    pen.up() 
    pen.setpos(x, y)
    pen.down()

    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(140)
    pen.forward(11.2 * größe + 1)
    kurve(größe)
    pen.left(120)
    kurve(größe)
    pen.forward(11.2 * größe)
    pen.end_fill()
    pen.right(220)
  
for x in range(100):
    herz(random.randint(-400, 400), random.randint(-300,300), random.randint(2,11), colors[random.randint(0, 7)])

pen.ht()
turtle.Screen().exitonclick()
