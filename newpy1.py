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
    drawSquare(alex, 20*(i+1))
    alex.penup()
    alex.setpos(-10*(i+1),-10*(i+1))
    alex.pendown()

wn.exitonclick()