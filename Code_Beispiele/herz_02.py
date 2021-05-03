import turtle
pen = turtle.Turtle()
  
def kurve(größe):
    for i in range(200):
        pen.right(1)
        pen.forward(.1 * größe)
  
def herz(x, y, größe):
    pen.up() 
    pen.setpos(x, y)
    pen.down()

    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(11.2 * größe + 1)
    kurve(größe)
    pen.left(120)
    kurve(größe)
    pen.forward(11.2 * größe)
    pen.end_fill()
    pen.right(220)
  
herz(-150, 150, 10)
herz(-130, 110, 9)
herz(-110, 70, 8)
herz(-90, 30, 7)
herz(-70, -10, 6)
herz(-50, -50, 5)
herz(-30, -90, 4)
herz(-10, -130, 3)

pen.ht()
turtle.Screen().exitonclick()
