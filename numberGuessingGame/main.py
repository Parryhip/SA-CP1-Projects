#Samuel Andelin, Number Guessing Game
import random
numtoguess = random.randint(1,100)
print("I'm thinking of a number between 1 and 100. Try to guess it.")
userguessedit = False
while userguessedit == False:
    userguess = input("What is your guess for the number?: ")
    userguessint = int(userguess)
    if userguessint < numtoguess:
        print("Too low.")
    elif userguessint > numtoguess:
        print("Too high.")
    elif userguessint == numtoguess:
        print("You guessed the number!")
        userguessedit = True