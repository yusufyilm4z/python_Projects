import turtle

#first shape
def drawSpiral(t,sz):
  t.right(90)
  for i in range(60):
    t.forward(sz)
    sz=sz+3
    t.right(90)

wn=turtle.Screen()
wn.bgcolor("purple")
donatello=turtle.Turtle()
donatello.color("lightgreen")
donatello.speed(20)
donatello.pensize(2)
donatello.penup()
donatello.backward(150)
donatello.pendown()

drawSpiral(donatello,2)

#second shape
donatello.penup()
donatello.home()
donatello.forward(90)
donatello.pendown()

def drawSpiral(t,sz):
  t.right(90)
  for i in range(60):
    t.forward(sz)
    sz=sz+3
    t.right(91)
drawSpiral(donatello,2)

wn.exitonclick()