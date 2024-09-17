#Samuel Andelin, Graded Quiz for Booleans
useranswer1 = int(input("What is the log base 10 of 10? "))
useranswer2 = int(input("What is the square root of 144? "))
useranswer3 = int(input("World population rounded to the nearest billion? "))
useranswer4 = int(input("How many biochemical reactions occur in the human body in one second?"))
useranswer5 = float(input("Pi rounded to the nearest 1000000th:"))
answer1 = 1
answer2 = 12
answer3 = 8000000000
answer4 = 37000000000000000000000
answer5 = 3.1415927
score = 0
if useranswer1 == answer1:
    score += 1
    print("Question 1 is correct!")
else:
    print("Question 1 is incorrect.")
if useranswer2 == answer2:
    score += 1
    print("Question 2 is correct!")
else:
    print("Question 2 is incorrect.")
if useranswer3 == answer3:
    score += 1
    print("Question 3 is correct!")
else:
    print("Question 3 is incorrect.")
if useranswer4 == answer4:
    score += 1
    print("Question 4 is correct!")
else:
    print("Question 4 is incorrect.")
if useranswer5 == answer5:
    score += 1
    print("Question 5 is correct!")
else:
    print("Question 5 is incorrect.")
print("Your score is " + str(score))