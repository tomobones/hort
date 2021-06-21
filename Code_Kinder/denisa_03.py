import turtle
def stern_klein():
    pen.begin_fill()
    for i in range(5):
        pen.color("orange")
        pen.forward(5)
        pen.left(144)
    pen.end_fill()
def  stern_mittel():
     for i in range(5):
         for j in range(10):
             stern_klein()
             pen.up()
             pen.forward(5)
             pen.down()
         pen.left(144)

def stern_gross():
    for i in range(5):
        for j in range(10):
            stern_mittel()
            pen.up()
            pen.forward(50)
            pen.down()
        pen.left(144)

pen = turtle.Turtle()
pen.up()
pen.setpos(-300,0)
pen.right(144)
pen.down()
stern_gross()

pen.ht()
turtle.Screen().exitonclick()
