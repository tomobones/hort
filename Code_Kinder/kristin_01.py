import  turtel

colors = ['red' , 'purple' , 'blue' , 'green' , 'yellow' , 'orange' ]

t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100
