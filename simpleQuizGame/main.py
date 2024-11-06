#Samuel Andelin, Simple Quiz Game
score = 0
question1 = input("What is the capital of Russia? \nA) Russia\nB) Moscia\nC) Moscow\nD) Greenland \n-->")
if question1.capitalize() == "A":
    print("You got it right!")
    score += 1
    question2 = input("What is the capital of Kansas? \nA) Salt Lake City\nB) Topeka\nC) Washington D.C.\nD) Houston \n-->")
    if question2.capitalize == "B":
        print("You got it right!")
        score += 1
    else:
        print("Incorrect. :( ")
else:
    print("Incorrect. :( ")
    question3 = input("What is the capital of Texas? \nA) Houston\nB) Boston\nC) Texas City\nD) Generald \n-->")
    if question3.capitalize() == "A":
        print("You got it right!")
        score += 1
    else:
        print("Incorrect. :( ")

question4 = input("What is the capital of Utah? \nA) Houston\nB) Washington D.C.\nC) Salt\nD) Salt Lake City \n-->")
if question4.capitalize() == "D":
    print("You got it right!")
    score += 1
else:
    print("Incorrect. :( ")