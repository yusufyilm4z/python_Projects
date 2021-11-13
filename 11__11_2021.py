mark=int(input("Please enter your grade: "))

def grade(mark):
    if (mark>=90):
        return "A"
    elif (mark>=80):
        return "B"
    elif (mark>=70):
        return "C"
    elif (mark>=60):
        return "D"
    elif (mark>=50):
        return "F"
    else:
        print("you fucked up with this lesson.")
print(grade(mark))
