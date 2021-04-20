import turtle
t = turtle.Pen()
number = eval(input("Wieviele Kreise willst du? "))
for x in range(number):
    t.circle(100)
    t.left(360/number)

turtle.Screen().exitonclick()
