import turtle

def drawFivePointStar(t,sz):
    for i in range(5):
        t.pendown()
        for j in range(5):
            t.forward(100)
            t.left(216)
        t.penup()
        t.left(36)
        t.forward(100)
wn=turtle.Screen()
wn.bgcolor("indigo")
thomas=turtle.Turtle()
thomas.color("cyan")
thomas.speed(5)
thomas.pensize(3)
thomas.fillcolor("red")
thomas.setpos(-150,20)

drawFivePointStar(thomas,50)
wn.exitonclick()


