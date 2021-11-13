import turtle

def drawSomething(t,sz):
  
    for i in range(4):
      t.forward(sz)
      t.left(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.speed(20)
alex.color("purple")
alex.pensize(3)

for j in range(20):
  drawSomething(alex,75)
  alex.left(18)

wn.exitonclick()
