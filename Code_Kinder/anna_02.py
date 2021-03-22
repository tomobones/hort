import turtle


colors=['magenta3','dark violet','cyan2','RoyalBlue2']
t=turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x%4])
    t.width(x/100+1)
    t.forward(x)
    t.left(11)
