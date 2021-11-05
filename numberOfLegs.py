import turtle
wn=turtle.Screen()
t=turtle.Turtle()

n = int(input("Enter the number of legs: "))

for i in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360/n)