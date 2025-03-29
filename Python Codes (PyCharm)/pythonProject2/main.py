#Calculate the volume of cuboid

# length = float(input("Enter the length of a cuboid : "))
# width = float(input("Enter the width of cuboid : "))
# height = float(input("Enter the height of cuboid : "))
#
# volume = length * width * height
#
# print(f"The volume of cuboid is {volume} cubic units.")



# Calculate the volume of cube
# side = float(input("Enter side of cubes : "))
#
# volume = side ** 3
# print(f"The volume of the cube is {volume} cubic units.")




#Calculate the area of rectangle
# length = float(input("Enter the length of the rectangle : "))
# width = float(input("Enter the width of rectangle : "))
#
# area = length * width
# print(f"The area of rectangle {area} square units")




# Calculate area of circle
# import math
# radius = float(input("Enter the radius of the circle : "))
#
# area = math.pi * (radius ** 2 )
# print(f"The area of the circle is {area} square units: ")


# Calculator for arithmetic operator
# a = float(input("Enter the number 1 : "))
# b = float(input("Enter the number 2 : "))
# operands = input("Enter the operand what to use(+,-,*,/,%,**,//) :")
#
# if operands == '+':
#     print("Num1 + Num2 = ",a+b)
# elif operands == '-':
#     print("Num1 - Num2 = ",a-b)
# elif operands == '*':
#     print("Num1 * Num2 = ",a*b)
# elif operands == '/':
#     print("Num1 / Num2 = ",a/b)
# elif operands == '%':
#     print("Num1 % Num2 = ",a%b)
# elif operands == '**':
#     print("Num1 ** Num2 = ",a**b)
# elif operands == '//':
#     print("Num1 // Num2 = ",a//b)


# Compare two number using relational operator

# a = int(input("Enter the first Number1 : "))
# b = int(input("Enter the second Number2 : "))
# c = input("Enter the relational operator : ")

# if c == '>' or c == '<':
#     if a>b:
#         print(f"{a} is greater than {b}")
#     elif a<b:
#         print(f"{a} is smaller than {b}")
#     elif a==b:
#         print(f"{a} is equal to {b}")
#     else:
#         print("We don't know")


# fruits = ["apple","banana","orange"]
# print(fruits[0])


# i = 1
# while i <= 5:
#     print(i)
#     i=i+1
# print("Done")

""""
Def Function

A function is a block of code that performs a specific task. Functions help in organizing
code, making it reusable and easier to understand.

Functions are created by using def keyword
The function signature should contain the function nature followed by the input parameters
enclosed in brackets and must end with a colon(:)

The function end with a return statement. No return statement implies the function return none.

"""
# def addElement(a,b=4):
#     return a + b
# print(addElement(2,5))




""""
# List
List are like array, but can contain hetrogeneous items that is a single list can
contain items of type integer, float, strings, or objects.
"""
# Batsmen = ["Rohit", "Kohli", "Dhawan", "Dhoni", "Rayudu", "Rahane"]
# print(Batsmen[0:3])
# print(Batsmen[-1])
# print(len(Batsmen))
#
# bowlers = ["Bumrah", "Shami", "Bhuvi", "Kuldeep", "Chahal"]

# all_players = Batsmen + bowlers
# print(all_players)
#
# print("Bumrah" in bowlers)
# print("Rayudu" in Batsmen)
#
# print(all_players.index('Dhoni'))
#
# all_players.reverse()
# print(all_players)






"""
Tuples 
Tuples is also a list but it is immutable. Once a tuple has been created it cannot be modified.
Tuple elements index also start with 0
An existing list can be converted into tuple using tuple type cast. We Convert the list all_players into
tuple so that it cannot be modified anymore.
"""
# odiDebut = ('Kohli', 2008)
# print(odiDebut)
# print(odiDebut[0])



"""
Set
A set is a collection of unique elements that is, the value cannot repeat.
A set can be initialized with a list of items enclosed with curly brackets.
"""
# setOfNumbers = {2,3,5,4,1,6,1}
# print(setOfNumbers)
#The set automatically remove duplicates and contain only unique list of numbers
"""
To understand these operation, let us create two sets with list list of
batsmen who played for india in 2011 and 2015 world cup teams.
"""
wc2011 = {"Dhoni", "Sehwag", "Tendulkar", "Gambhir", "Kohli", "Raina", "Yuvraj", "Yusuf"}
wc2015 = {"Dhoni", "Dhawan", "Rohit", "Rahane", "Kohli", "Raina", "Rayudu", "Jadeja"}

# To find the list of all batsmen who played in either 2011 or 2015 world cup, we can take union of the above two sets
# print(wc2011.union(wc2015))




"""
Dictionary 
Dictionary is a list of key and value pairs.All the keys in a dictionary are unique.\



"""


# price = 100
# price *= 0.9
# print("Price after 10%discount : ",price)
# price -= 5
# print("Find price after Rs. 5 deduction : ",price)


# Volume of cuboid
# len = float(input("Enter the length of the cuboid: "))
# wid = float(input("Enter the width of the cuboid: "))
# hght = float(input("Enter the height of the cuboid: "))
#
# vol = len * wid * hght
#
# print("The volume of the cuboid is : ",vol)
#

# Volume of cube
# side = float(input("Enter the side of cube: "))
# vol = side ** 3
# print("The volume of the cube is: ",vol)

# Area of the rectangle
# len = float(input("Enter the Length of the rectangle : "))
# wid = float(input("Enter the width of thje rectangle: "))
# area = len * wid
# print("The Volume of the cuboid is : ",area)

# Area of the circle
# import math
# r = float(input("Enter the radius of the circle is : "))
# area = math.pi * (r**2)
# print(f"The Area of the circle is {area}")

# cel = float(input("Enter temperature in celsius: "))
#
# fahr = (cel * 9/5)+32
# print(f"The temperature in fahrenheit: {fahr}")


# Arithemetic operator
# num1 = int(input("Enter the Number1: "))
# num2 = int(input("Enter the Number2: "))
#
# operand = input("Enter hte operand(+,-,*,/,%,**,//): ")
#
# if operand == "+":
#     print(f"Num1 + Num2 = {num1 + num2}")
# if operand == "-":
#     print(f"Num1 - Num2 = {num1 - num2}")
# if operand == "*":
#     print(f"Num1 * Num2 = {num1 * num2}")
# if operand == "/":
#     print(f"Num1 / Num2 = {num1 / num2}")
# if operand == "%":
#     print(f"Num1 % Num2 = {num1 % num2}")
# if operand == "**":
#     print(f"Num1 ** Num2 = {num1 ** num2}")
# if operand == "//":
#     print(f"Num1 // Num2 = {num1 // num2}")

# Python program to biggest Number
a = int(input)





















