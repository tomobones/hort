import turtle

colors=[ 'purple','hot pink','deep pink','pink','pale violet pink','maroon','mediom violet pink','medium ochid']
t=turtle.Pen()
turtle.bgcolor('cyan2')
for x in range(333):
    t.pencolor(colors[x%3])
    t.width(222+45454)
    t.forward(x)
    t.left(33)
turtle.Screen().exitonclick()

	
