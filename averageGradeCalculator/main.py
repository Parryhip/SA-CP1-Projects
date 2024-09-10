#Samuel Andelin, Average Grade
grade1 = input("What is your 1st period grade?: ")
grade2 = input("What is your 2nd period grade?: ")
grade3 = input("What is your 3rd period grade?: ")
gradeadvisory = input("What is your advisory period grade?: ")
grade6 = input("What is your 6th period grade?: ")
grade7 = input("What is your 7th period grade?: ")
grade8 = input("What is your 8th period grade?: ")
averagegrade = (int(grade1) + int(grade2) + int(grade3) + int(gradeadvisory) + int(grade6) + int(grade7) + int(grade8))/7
print("Your average grade is: "+str(averagegrade))