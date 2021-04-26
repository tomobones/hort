import turtle
pen =turtle.Turtle()

def kurve():
   for i in range(200):
       pen.right(1)
       pen.forward(2)

def herz():
   pen.fillcolor('medium orchid')
   pen.begin_fill()

   pen.left(140)
   pen.forward(225)
   kurve()
   pen.left(120)
   kurve()
   pen.forward(224)
   pen.end_fill()


def text():
   pen.color('firebrick1')
   pen.up()
   pen.setpos(-110, 50)
   pen.down()
   pen.write("Alles Gute zum Muttertag", font=("Verdana",12, "bold"))

   pen.up()
   pen.setpos(-40, 20)
   pen.down()
   pen.write("Deine Denisa", font=("Verdana", 12, "bold"))

pen.up()
pen.setpos(0, -150)
pen.down()

herz()
text()
pen.ht()
turtle.Screen().exitonclick()
