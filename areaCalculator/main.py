#Samuel Andelin, Area Calculator
import math
def squarearea():
    squareheight = input("What is the height of the square?: ")
    print("The area of the square is " + str(int(squareheight)**2))
def rectanglearea():
    rectangleheight = input("What is the height of the rectangle?: ")
    rectanglewidth = input("What is the width of the rectangle?: ")
    print("The area of the rectangle is "+ str(int(rectangleheight)*int(rectanglewidth)))
def trianglearea():
    triangleheight = input("What is the height of the triangle?: ")
    trianglewidth = input("What is the width of the triangle?: ")
    print("The area of the triangle is "+ str((int(triangleheight)*int(trianglewidth))/2))
def circlearea():
    circleradius = input("What is the radius of the circle?: ")
    print("The area of the circle is "+ str(math.pi*(int(circleradius)**2)))
def trapezoidarea():
    trapezoidheight = input("What is the height of the trapezoid?: ")
    trapezoidwidth1 = input("What is the top width of the trapezoid?: ")
    trapezoidwidth2 = input("What is the bottom width of the trapezoid?: ")
    print("The area of the trapezoid is "+str(((int(trapezoidwidth1)+int(trapezoidwidth2))/2)*int(trapezoidheight)))
typeofshape = input("Input the shape you want to find the area of (1/2/3/4/5) \n 1. Calculate area of square. \n 2. Calculate area of rectangle. \n 3. Calculate area of triangle. \n 4. Calculate area of circle. \n 5. Calculate area of trapezoid.   --> ")
if typeofshape == "1":
    squarearea()
elif typeofshape == "2":
    rectanglearea()
elif typeofshape == "3":
    trianglearea
elif typeofshape == "4":
    circlearea()
elif typeofshape == "5":
    trapezoidarea()
else:
    print("Invalid input.")