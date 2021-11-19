def isThreeAngle(k,l,m):
    isThreeAngle=False
    if k>l and k>m:
        isThreeAngle=abs(l**2 + m**2 - k**2) < 0.001
    elif l>k and l>m:
        isThreeAngle=abs(k**2 + m**2 - l**2) < 0.001
    else:
        isThreeAngle=abs(k**2 + l**2 - m**2) < 0.001
    return isThreeAngle
k=int(input("k value is: "))
l=int(input("l value is: "))
m=int(input("m value is: "))

print(isThreeAngle(k,l,m))