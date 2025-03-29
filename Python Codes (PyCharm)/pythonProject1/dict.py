def greet(name, good, issues):
    message = f"hello, {name}! How was your day? It was {good}. Did you face major issues? {issues}!"
    return message

name_input = input("Enter your name: ")
day_input = input("Was your day good or bad: ")
if day_input.lower() == "good":
    print("congrats, you survived another day!")
if day_input.lower() == "bad":
    print("what works better than goooooood mooooorningggg")
issues_input = input("Had major issues (no or yes): ")
if issues_input.lower() == "no":
    print("stay happy like this forever,hehe")
if issues_input.lower() == "yes":
    print("awww, that's sad, but tomorrow will be amazing, don't worry")
print(greet(name_input, day_input, issues_input))
