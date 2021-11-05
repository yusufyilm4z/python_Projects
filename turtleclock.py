import turtle
wn=turtle.Screen()
t=turtle.Turtle()

t.shape("turtle")
turtle.color(input("Please enter the turtle color: "))
turtle.bgcolor(input("Please enter the background color: "))
t.stamp()
for i in range(12):
  t.penup()
  t.forward(100)
  t.stamp()
  t.backward(100)
  t.left(30)
wn.exitonclick()