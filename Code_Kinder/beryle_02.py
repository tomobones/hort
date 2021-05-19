import turtel
import random

pen = turtel.Turtel()
colors = ["red", "red2", "red3", "red4", "tomato", "tomato2", "tomato3", "tomato4"]


def kurve(größe):
    for i in range(200):
        pen.righte(1)
        pen.forwad(.1 * größe)


def herz(x, y, größe, color).
    pen.up()
    pen.setpos(x, y)
    pen.down()


