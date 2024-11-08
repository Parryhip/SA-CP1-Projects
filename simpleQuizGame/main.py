#Samuel Andelin, Simple Quiz Game
score = 0
question1 = input("What is the capital of Russia? \nA) Russia\nB) Moscia\nC) Moscow\nD) Greenland \n-->")
if question1.capitalize() == "B":
    print("You got it right!")
    score += 1
    print("Your score is "+str(score))
    question2 = input("What is the capital of Kansas? \nA) Salt Lake City\nB) Topeka\nC) Washington D.C.\nD) Houston \n-->")
    if question2.capitalize == "B":
        print("You got it right!")
        score += 1
        print("Your score is "+str(score))
    else:
        print("Incorrect. :( ")
else:
    print("Incorrect. :( ")
    question3 = input("What is the capital of Texas? \nA) Houston\nB) Boston\nC) Texas City\nD) Generald \n-->")
    if question3.capitalize() == "A":
        print("You got it right!")
        score += 1
        print("Your score is "+str(score))
    else:
        print("Incorrect. :( ")

question4 = input("What is the capital of Utah? \nA) Houston\nB) Washington D.C.\nC) Salt\nD) Salt Lake City \n-->")
if question4.capitalize() == "D":
    print("You got it right!")
    score += 1
    print("Your score is "+str(score))
    question6 = input("What is the capital of Massachusetts? \nA) Houston\nB) Boston\nC) Texas City\nD) Generald \n-->")
    if question6.capitalize() == "B":
        print("You got it right!")
        score += 1
        print("Your score is "+str(score))
    else:
        print("Incorrect. :( ")
else:
    print("Incorrect. :( ")
    question5 = input("What is the capital of the United States? \nA) Houston\nB) Washington D.C.\nC) Salt\nD) Salt Lake City \n-->")
    if question5.capitalize() == "B":
        print("You got it right!")
        score += 1
        print("Your score is "+str(score))
    else:
        print("Incorrect. :( ")

final_question = input("What is the capital of the Slovenia? \nA) Frensaies\nB) Hcdfegsa D.C.\nC) Ljubljana\nD) Brazil \n-->")
if final_question.capitalize() == "C":
    print("You got it right!")
    score += 1
    print("Your score is "+str(score))
else:
    print("Incorrect. :( ")
print("Your final score is "+str(score))