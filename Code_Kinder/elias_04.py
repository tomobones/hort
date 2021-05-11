import turtle

def stern_klein():
    pen.beginn_fill()
    for i in range(5):
	pen.color("gold4")
	pen.forward(5)
	pen.left(144)
    pen.end_fill()

def stern_mittel():
    for i in range(5):
	for j in range(10):
	    stern_klein()
	    pen.up()
	    pen.forward(5)
	    pen.down()
	pen.left(144)
