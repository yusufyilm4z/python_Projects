name=input("What is your name?: ")
print("Welcome to the hangman game", name.capitalize())
startGame=input("Do you want to start the game(Yes/No): ")
if startGame.capitalize() == "Yes":
  print("Let's begin!")
  theWord=input("Please enter your secret word: ")
elif startGame.capitalize() == "No":
  print("Then, see you next time.")
else:
  print("Sorry, I cannot understand that.")


#it will be complete soon...