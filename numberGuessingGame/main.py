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
    #changing the user's input into an integer for easier checking
    userguessint = int(userguess)
    #if the user's guess is too high
    if userguessint < numtoguess:
        #print that the user's guess is too high
        print("Too low.")
    #if the user's guess is too low
    elif userguessint > numtoguess:
        #print that the user's guess is too low
        print("Too high.")
    #if the user's guess is correct(it is the same as the random number)
    elif userguessint == numtoguess:
        #print that the user won / guessed the number
        print("You guessed the number!")
        #sets that the user has guessed the number
        userguessedit = True