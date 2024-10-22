#Samuel Andelin, Rock Paper Scissors Proficiency
import random
import time
def whowon(plyr, comp):
    if plyr == comp:
        print("It's a tie!")
        return "tie"
    elif plyr == "r" and comp == "s":
        return "user"
    elif plyr == "s" and comp == "p":
        return "user"
    elif plyr == "p" and comp == "r":
        return "user"
    elif plyr == "p" and comp == "s":
        return "comp"
    elif plyr == "r" and comp == "p":
        return "comp"
    elif plyr == "s" and comp == "r":
        return "comp"
def main():
    userscore = 0
    compscore = 0
    print("Welcome to rock, paper, scissors!")
    while True:
        choice = input("Type r for rock, p for paper, s for scissors, and q for quit.")
        if choice == "r":
            print("You chose rock.")
            time.sleep(1)
            print("Computer is playing...")
            time.sleep(2)
            compchoice = random.randint(1, 3)
            if compchoice == 1:
                compchoicemod = "r"
                print("The computer chose rock.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 2:
                compchoicemod = "p"
                print("The computer chose paper.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 3:
                compchoicemod = "s"
                print("The computer chose scissors.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
        elif choice == "p":
            print("You chose paper.")
            time.sleep(1)
            print("Computer is playing...")
            time.sleep(2)
            compchoice = random.randint(1, 3)
            if compchoice == 1:
                compchoicemod = "r"
                print("The computer chose rock.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 2:
                compchoicemod = "p"
                print("The computer chose paper.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 3:
                compchoicemod = "s"
                print("The computer chose scissors.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
        elif choice == "s":
            print("You chose scissors.")
            time.sleep(1)
            print("Computer is playing...")
            time.sleep(2)
            compchoice = random.randint(1, 3)
            if compchoice == 1:
                compchoicemod = "r"
                print("The computer chose rock.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 2:
                compchoicemod = "p"
                print("The computer chose paper.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
            elif compchoice == 3:
                compchoicemod = "s"
                print("The computer chose scissors.")
                if whowon(choice, compchoicemod) == "tie":
                    print("It's a tie!")
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "user":
                    print("You won!")
                    userscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
                elif whowon(choice, compchoicemod) == "comp":
                    print("Computer won!")
                    compscore += 1
                    print("The score is user["+str(userscore)+"] to comp["+str(compscore)+"].")
        elif choice == "q":
            print("Ok, bye!")
            break
        else:
            print("Not a valid answer. Please try again.")
            continue
main()