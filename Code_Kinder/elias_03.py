import turtle

colors=['aquamarine2', 'cyan3', 'LightGoldenrod3']
t=turtle.Pen()
turtle.bgcolor('snow')
for x in range(360):
	t.pencolor(colors[x%3])
	t.width(x/100+1)
	t.forward(x)
	t.left(59)
