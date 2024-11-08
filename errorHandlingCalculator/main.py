#Samuel Andelin, Error Handling Calculator
while True:
    number1 = input("What should the first number be?: ")
    number2 = input("What should the second number be?: ")
    try:
        num = int(number1)
        num = int(number2)
        break
    except:
        print("Please input integers.")
operation = input("What operation should I run(a for add, b for subtract, c for multiply, d for divide, e for exponent, f for modulo, g for rounded division)?: ")
if operation == "a":
  print(str(number1) + " + "+str(number2) +" = "+str(int(number1) + int(number2)))
elif operation == "b":
  print(str(number1) + " - "+str(number2) +" = "+str(int(number1) - int(number2)))
elif operation == "c":
  print(str(number1) + " * "+str(number2) +" = "+str(int(number1) * int(number2)))
elif operation == "d":
  print(str(number1) + " / "+str(number2) +" = "+str(int(number1) / int(number2)))
elif operation == "e":
  print(str(number1) + " to the power of "+str(number2) +" = "+str(int(number1) ** int(number2)))
elif operation == "f":
  print(str(number1) + " modulo "+str(number2) +" = "+str(int(number1) % int(number2)))
elif operation == "g":
  print(str(number1) + " / "+str(number2)+ "rounded = "+str(int(number1) // int(number2)))
else:
  print("Not valid input. Restart program.")