import math
x=float(int(input("please enter the x side: ")))
y=float(int(input("please enter the y side: ")))
hyphotenuse=(math.pow(x,2) + math.pow(y,2)) ** 0.5
hyphotenuse=math.hypot(x,y)
print(hyphotenuse)
