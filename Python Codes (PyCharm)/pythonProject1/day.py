def greet(name, good, issues):
    message = f"hello, {name}! How was your day? It was {good}. Did you face major issues? {issues}!"
    return message

name_input = input("Enter your name: ")
day_input = input("Your day was good or bad: ")
if day_input.lower() == "good":
    print("congrats, you survived another day!")
if day_input.lower() == "bad":
    print("what works better than goooooood mooooorningggg")
issues_input = input("Had major issues (no or yes): ")

# Call the greet function with the inputs
print(greet(name_input, day_input, issues_input))