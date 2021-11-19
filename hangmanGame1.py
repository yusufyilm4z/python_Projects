import random
answerList='''ant baboon badger bat bear beaver camel cougar cat 
clam cobra coyote crow deer dog donkey'''.split()

answer = list(random.choice(answerList))
print(answer)

display = answer.copy()
for index in range(len(display)):
    display[index]="_"

print(display)
print(" ".join(display))

incorrect = 6
correct = 0
previousGuesses=[]

while incorrect > 0 and correct < len(display):
    ...

if (incorrect==0):
    print("you lose the game.")
else:
    print("Well done! you won the game.")
exit()
