import math
#Calculator does basic equations as well as sin, cos, tan, and sqrt.

#Give user instructions on how to use the calculator
def calc():
#input lets user select an option
  user_input = input("Welcome to the calculator! \nType a for sin,\n b for cos,\n c for tan,\n d for sqrt.\n Else, type the equation you want to solve\n(+ for add,\n - for subtract,\n / for divide,\n * for multiply,\n // for rounded down to integer value of \n division problem,\n ** for exponentation,\n % for modulo): ")
  #if statement checking for sin and my sin output
  if user_input == "a":
    sin = input("What number should I run the sin function on?")
    print("The sin of "+sin+" is "+ str(math.sin(int(sin))))
    calc()
  
  #if statement checking for cos and my cos output
  elif user_input == "b":
    cos = input("What number should I run the cos function on?")
    print("The cos of "+cos+" is "+ str(math.cos(int(cos))))
    calc()
  #if statement checking for tan and my tan output
  elif user_input == "c":
    tan = input("What number should I run the tan function on?")
    print("The tan of "+tan+" is "+ str(math.tan(int(tan))))
    calc()
  #if statement checking for sqrt and my sqrt output
  elif user_input == "d":
    sqrt = input("What number should I run the sqrt function on?")
    print("The sqrt of "+sqrt+" is "+ str(math.sqrt(int(sqrt))))
    calc()
  #else print an eval of my user input
  else:
    print(" = " + str(eval(user_input)))
    calc()

calc()