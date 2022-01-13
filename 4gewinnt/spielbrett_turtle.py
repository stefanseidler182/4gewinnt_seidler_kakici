import turtle
x = 50
y = 650
turtle.setworldcoordinates(0, 0, 800, 700)
a = turtle.Turtle()
a.pencolor("blue")
a.hideturtle()
a.speed(0)
a.penup()
a.goto(x, y)
a.pendown()
i = 0
j = 0
a.fillcolor("blue")
a.begin_fill()
a.forward(700)
a.right(90)
a.forward(600)
a.right(90)
a.forward(700)
a.right(90)
a.forward(600)
a.right(90)
a.end_fill()
x = 100
y = 560
while i < 6:
    a.pencolor("white")
    while j < 7:
        a.penup()
        a.fillcolor("white")
        a.begin_fill()
        a.goto(x, y)
        a.pendown()
        a.circle(40)
        a.end_fill()
        x += 100
        j += 1
    y -= 100
    x = 100
    j = 0
    i += 1

turtle.exitonclick()