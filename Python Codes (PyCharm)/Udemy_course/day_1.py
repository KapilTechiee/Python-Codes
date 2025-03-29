# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# if num1 > num2:
#     print("num1 is greater than num2")
# elif num2 > num1:
#     print("num2 is greater than num1")
# else:
#     print("num1 equal to num2")
#     `
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
#
# if num1 > num2 and num1 > num3:
#     print("num1 is grater than two numbers")
# elif num2 > num3 and num2>num1:
#     print("num2 is grater than two numbers")
# else:
#     print("num3 is greater two numbers")
#
# num = int(input("Enter number : "))
# if num % 2 ==0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
#
# i = 1
# while(i<=10):
#     print(i)
#     i=i+1
#
# i = 10
# while(i>=1):
#     print(i)
#     i=i-1
from sys import flags

num = 1
while(num <= 100):
    if(num % 2 == 0):
        print("This is an even number",num)

    else:
        print("This is an odd number",num)
    num = num+1



num = int(input("Enter a number : "))
i = 2
flag = 0
while i <num:
    if(num%2==0):
        flag = 1
    i=i+1
if(flag ==0):
    print(num,"This is prime")
else:
    print(num,"This is not prime")























