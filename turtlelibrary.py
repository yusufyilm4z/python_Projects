import turtle
wn= turtle.Screen()
rafael=turtle.Turtle()

numberOfSides=int(input("Please enter the number of sides: "))
sideLenght=int(input("Please enter the lenght of sides: "))
angle=360/numberOfSides
color= input("Please enter the color: ")
fillColor= input("Please enter the fill color: ")
rafael.color(color)
rafael.fillcolor(fillColor)

rafael.begin_fill()
for i in range(numberOfSides):
    rafael.forward(sideLenght)
    rafael.left(angle)
rafael.end_fill()
wn.exitonclick()