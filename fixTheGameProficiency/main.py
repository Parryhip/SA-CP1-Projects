#Samuel Andelin, Fix The Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))#The bug was that the computer can't compare integers and strings. This is a runtime error. If the computer can't compare strings and integers, then it won't know if you are too high, too low, or right.
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess: 
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess: 
            print("Too high! Try again.")
            attempts += 1 #The bug was that the computer didn't know when the user's attempts ran out. This is a logic error. If the computer doesn't know if the user has used up all of their attempts, then the user can just spam random numbers with no consequence of losing.
        elif guess < number_to_guess: 
            print("Too low! Try again.")  
            attempts += 1 #Needed to increase the attempts variable to actually control the attempts
        continue
    print("Game Over. Thanks for playing!")
start_game()