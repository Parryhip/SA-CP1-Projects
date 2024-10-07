#Samuel Andelin, Number Guessing Game
#get random database
import random
#chooses random number
numtoguess = random.randint(1,100)
#user instructions
print("I'm thinking of a number between 1 and 100. Try to guess it.")
#sets that the user hasn't guessed the number yet
userguessedit = False
#while loop until the user guesses the number
while userguessedit == False:
    #user prompt for number
    userguess = input("What is your guess for the number?: ")
    userguessint = int(userguess)
    if userguessint < numtoguess:
        print("Too low.")
    elif userguessint > numtoguess:
        print("Too high.")
    elif userguessint == numtoguess:
        print("You guessed the number!")
        userguessedit = True