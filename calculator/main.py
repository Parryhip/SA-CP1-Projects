#Samuel Andelin, Simple Calculator
number1 = int(input("What should the first number be?: "))
number2 = int(input("What should the second number be?: "))
operation = input("What operation should I run(a for add, b for subtract, c for multiply, d for divide, e for exponent, f for modulo, g for rounded division)?: ")
if operation == "a":
  print(str(number1) + " + "+str(number2) +" = "+str(number1 + number2))
elif operation == "b":
  print(str(number1) + " - "+str(number2) +" = "+str(number1 - number2))
elif operation == "c":
  print(str(number1) + " * "+str(number2) +" = "+str(number1 * number2))
elif operation == "d":
  print(str(number1) + " / "+str(number2) +" = "+str(number1 / number2))
elif operation == "e":
  print(str(number1) + " to the power of "+str(number2) +" = "+str(number1 ** number2))
elif operation == "f":
  print(str(number1) + " modulo "+str(number2) +" = "+str(number1 % number2))
elif operation == "g":
  print(str(number1) + " / "+str(number2)+ "rounded = "+str(number1 // number2))
else:
  print("Not valid input. Restart program.")