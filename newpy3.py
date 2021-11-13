import turtle
wn=turtle.Screen()

track=turtle.Turtle()

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


wn.exitonclick()