def isEven(n):
    while True:
        if n%2 == 0:
            return True
        else:
            return False
    return n
while True:
    n=int(input("The number is: "))
    print(isEven(n))
    