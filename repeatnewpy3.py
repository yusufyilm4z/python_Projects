import turtle
wn=turtle.Screen()

track=turtle.Turtle()
track.speed(20)

for i in range(15):
    track.write(i, align="center")
    track.right(90)
    for j in range(8):
        track.penup()
        track.forward(10)
        track.pendown()
        track.forward(10)
    track.penup()
    track.backward(160)
    track.left(90)
    track.forward(20)

track.hideturtle()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("cyan")
t1.setpos(-10, -20)
wn.exitonclick()