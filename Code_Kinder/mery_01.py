import tortel
import random

pen=turtel.Turtel()
colors=["red", "red2", "red3", "tomato", "tomato2", "tomato3", "tomato4"]

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
