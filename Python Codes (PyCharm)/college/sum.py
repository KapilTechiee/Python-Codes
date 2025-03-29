#first = int(input("Enter the First Number : "))
# second = int(input("Enter the Second Number : "))
# third = int(input("Enter third Number : "))
# if first > second:
#     print("First is greater ")
# elif second > third:
#     print("Second is greater ")
# if third > first:
#     print("Third is greater ")
# else:
#     print("Numbers are equal ")


num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
if (num1 >= num2) and  (num1 >= num3) :
    greatest = num1
elif (num2 >= num1) and (num2 >= num3) :
    greatest = num2
else :
    greatest = num3
print("The Maximum number is :",greatest)
















