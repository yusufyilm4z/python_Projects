import random

number=random.randrange(100,1000)
score=0
previousGuesses = []
while True:
    guess=int(input("Make a guess: "))
    print("Your previous guesses are:",previousGuesses)
    previousGuesses.append(guess)
    score+=1
    if (guess<number):
        print("Higher!")
        
    elif (guess>number):
        print("Lower!")
    else:
        print("You found the number: ")
        break