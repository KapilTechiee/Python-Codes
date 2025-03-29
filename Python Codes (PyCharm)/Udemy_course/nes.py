# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))
# operator = input("Enter the Operator(+,-,*,/,%)")
# if operator == '+':
#     print("The Sum of num1 + num2 =",a+b)
# elif operator == '+':
#     print("The Sub of num1 + num2 =",a-b)
# elif operator == '+':
#     print("The Mul of num1 + num2 =",a*b)
# elif operator == '+':
#     print("The Div of num1 + num2 =",a/b)
# elif operator == '+':
#     print("The Rem of num1 + num2 =",a%b)



# a = 1
# b = 2
# print("The Number before a & b =  ",a ,b)

# c = a
# a = b
# b = c
# print("The Number After a & b = ",a,b)



import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)  # Send a GET request
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert response to JSON
        return data["bitcoin"]["usd"]  # Extract price
    else:
        return "API Error!"

print(get_bitcoin_price())  # Output: 42,000 (example)
