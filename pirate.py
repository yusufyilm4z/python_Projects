import turtle

wn=turtle.Screen()
pirate=turtle.Turtle()

pirate.forward(100)
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)
wn.exitonclick
