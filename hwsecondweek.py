import turtle
wn=turtle.Screen()
Ivy=turtle.Turtle()

numberOfSides=int(input("Please enter the number of sides: "))
lenghtOfSides=int(input("Please enter the lenght of sides: "))
angle=360/numberOfSides
Ivy.pensize(3)
Ivy.color(input("Please enter side color: "))
Ivy.fillcolor(input("Please enter the color of your turtle: "))
Ivy.begin_fill()

for i in range(numberOfSides):
  Ivy.forward(lenghtOfSides)
  Ivy.left(angle)
Ivy.end_fill()
wn.exitonclick()