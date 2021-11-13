import turtle

def drawOctagon(t,sideNum,sideSize):
    for i in range(8):
        t.forward(sideSize)
        t.left(360/sideNum)

wn=turtle.Screen()
alex=turtle.Turtle()
drawOctagon(alex, 8, 30)

wn.exitonclick()
