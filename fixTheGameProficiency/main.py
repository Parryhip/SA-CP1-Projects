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
        attempts += 1 #The bug was that the computer didn't know when the user's attempts ran out. This is a logic error. If the computer doesn't know if the user has used up all of their attempts, then the user can just spam random numbers with no consequence of losing.
        guess = int(input("Enter your guess: "))#The bug was that the computer can't compare integers and strings. This is a runtime error. If the computer can't compare strings and integers, then it won't know if you are too high, too low, or right.
        if guess == number_to_guess:
            continue  #The bug was that the you can win and lose at the same time if you guess the right number on your last attempt. This is a logic error. If we can win and lose at the same time, there is no point to the last attempt.
        elif guess > number_to_guess: 
            print("Too high! Try again.")
        elif guess < number_to_guess: 
            print("Too low! Try again.")  
        elif attempts >= max_attempts: #The bug was that the computer checked if the user lost before it checked if the user won. This is a logic error. If we lose on our last attempt before we win, then there is again no point to the last attempt.
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
    print("Game Over. Thanks for playing!")
start_game()