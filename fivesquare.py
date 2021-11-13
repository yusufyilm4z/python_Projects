import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("purple")

alex = turtle.Turtle()
alex.color("lightgreen")
alex.pensize(3)

for i in range(5):
    drawSquare(alex, 20)
    alex.penup()
    alex.forward(40)
    alex.pendown()


wn.exitonclick()