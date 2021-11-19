def leapYear(theYear):
    if theYear%4==0 or theYear%400==0:
        if theYear%100==0:
            return False
        else:
            return True
    else:
        return False
while True:        
    theYear=abs(int(input("Please enter the year: ")))
    print(leapYear(theYear))