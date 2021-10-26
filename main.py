currentTime=input("What time is it right now?: ")
timerLenght=input("What is the timer lenght?: ")
totalTime= int(currentTime) + int(timerLenght)
print(totalTime%24)