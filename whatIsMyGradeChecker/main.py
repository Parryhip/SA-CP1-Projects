#Samuel Andelin, What Is My Grade
grade = int(input("What is the grade to turn into a letter grade?: "))
if grade >= 93:
    print("Your letter grade is an A!")
elif grade >= 90:
    print("Your letter grade is an A-!")
elif grade >= 87:
    print("Your letter grade is an B+!")
elif grade >= 83:
    print("Your letter grade is an B!")
elif grade >= 80:
    print("Your letter grade is an B-!")
elif grade >= 77:
    print("Your letter grade is an C+!")
elif grade >= 73:
    print("Your letter grade is an C!")
elif grade >= 70:
    print("Your letter grade is an C-!")
elif grade >= 67:
    print("Your letter grade is an D+!")
elif grade >= 65:
    print("Your letter grade is an D!")
elif grade >= 61:
    print("Your letter grade is an D-!")
else:
    print("Your letter grade is an F!")
