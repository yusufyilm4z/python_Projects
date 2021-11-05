import turtle
wn=turtle.Screen()
t=turtle.Turtle()

turtle.bgcolor("red")
t.fillcolor("red")
t.color("yellow")

t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

wn.exitonclick()