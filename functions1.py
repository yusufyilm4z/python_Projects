import turtle
def drawTriangle(t, sz):
  for i in range(3):
    t.forward(sz)
    t.left(120)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
adam=turtle.Turtle()
drawTriangle(adam, 150)

wn.exitonclick()