# Basic Syntax
#







# Day 1
# Brand Name Generator Code
# from random import random
from itertools import filterfalse
from statistics import multimode

# print("Welcome to the brand Name Generator!")
# city = input("What's the name of the city you grew up in: ")
# pet_name = input("What's your pet's name: ")
# print(f"Your brand name could be {city} {pet_name}")





# Day 2
# Tip Calculator

# print("Welcome to the tip Calculator!")
# bill = float(input("What was the total bill? $: "))
# tip = float(input("How much tip would you like to give? 10, 12, or 15"))
# split = int(input("How many person should pay?: $"))

# tip_per = tip / 100
# total_tip_amt = bill * tip_per
# total_bill = bill + total_tip_amt
# per_split = total_bill / split
# print("Each Person should to pay: ",per_split)








# Day 3 Logical Operator

# print('''*******************************************************************************
#          |                   |                  |                     |
#           _________|________________.=""_;=.______________|_____________________|_______
#          |                   |  ,-"_,=""     `"=.|                  |
#          |___________________|__"=._o`"-._        `"=.______________|___________________
#          |                `"=._o`"=._      _`"=._                     |
#          _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#          |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#          |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#          |                     |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#          _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
#           |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
#           |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#           ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
#           /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#           ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#           /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#           ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
#           /______/______/______/______/______/______/______/______/______/______/_____ /
#           *******************************************************************************
#              '‘’)
#
# print("Welcome to the Treasure Island\nYour mission is to find the ttreasure🪙")
# side1 = input("You have 2 side left or right where do you wad to go: ").lower()
# if side1 == "left":
#     do2 = input("You are now island you want to swim or wait for boat: ").lower()
# if do2 == "wait":
#         room3 = input("You are now at island there a house with the three room red,yellow,blue: ").lower()
#                 if room3 == "yellow":
#                     print("You Win Congratulations! ")
#                 elif room3 == "blue":
#                     print("Eaten by beasts Game Over")
#                 elif room3 == "red":
#                     print("Burned by fire")
#                 else:
#                     print("You Choose that door doesn't exist")
#         else:
#             print("Attacked by shark the game over")
# else:
#     print("you fell into a hole")







# Day 4 Randomisation & Python Lists

# import random
import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.my_favourite_number)

# random.random => Gives float number between 0 to 1.

# random_number_0to_1 = random.random() * 10
# print(random_number_0to_1)

# random.uniform => To print Float number we use random.uniform

# random_float = random.uniform(1,10)
# print(random_float)


# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")


# Lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# print(states_of_america[2])
# print(states_of_america[-1])
#
# states_of_america[1] = "Pencilvania"
#
# states_of_america.append("Angelaland")
#
# print(states_of_america)


# Rock Paper Scissor Game

# import random
# user_choice = int(input("What to do you want to choose? Type 0 for Rock, 1 for paper, 2 for Scissors: "))
# computer_choice = random.randint(0,2)
#
# print(f"Computer chose: {computer_choice}")
#
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number you lose!")
# else:
#     if user_choice == 0 and computer_choice == 2:
#         print("You Win")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You Lose!")
#     elif computer_choice > user_choice:
#         print("You Lose!")
#     elif user_choice > computer_choice:
#         print("you Win")
#     else:
#         print("It's Draw")


# Day 5


# fruits = ["Apple", "Peach", "Pear"]
# for fruits in fruits:
#     print(fruits)
#     print(fruits + " pie")
#     print(fruits)

# students_score = [150,142,180,162,158,124,199,189,187]
# total_exam_score = sum(students_score)
# print(total_exam_score)
# sum = 0
# for score in students_score:
#     sum += score
#
# print(sum)
#
# print(max(students_score))
#
# max_score = 0
# for score in students_score:
#     if score > max_score:
#         max_score = score
# print(max_score)

# Range function
# for number in range(1,11):
#     print(number)


# for number in range(1,11,2):
#     print(number)


# total = 0
# for number in range(1,101):
#     total += number
#
# print(total)


# Password Generator Project

# Easy Level

# print("Welcome to the password Generator")
# letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# number = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!','#','$','%','&','(',')','*','+']
#
#
# nr_letter = int(input("How many letters would you like in your password"))
# nr_symbol = int(input("How many symbol would you like?\n"))
# nr_number = int(input("How many number would you like?\n"))
#

# password = ""
# for char in range(0,nr_letter):
#     password += random.choice(letter)
#
# for char in range(0,nr_symbol):
#     password += random.choice(symbols)
#
# for char in range(0,nr_number):
#     password += random.choice(number)
#
# print(password)

# Hard Level

# import random
#
# print("Welcome to the password Generator")
# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!','#','$','%','^','&','*','(',')','_','-','@','~']
#
#
# nr_letter = int(input("How many letters would like in your password: "))
# nr_symbol = int(input("How many symbol would like in your password: "))
# nr_number = int(input("How many number would like in your password: "))
#
# password_list = []
#
# for char in range(0,nr_letter):
#     password_list.append(random.choice(letters))
# for char in range (0,nr_symbol):
#     password_list.append(random.choice(symbols))
# for char in range (0,nr_number):
#     password_list.append(random.choice(numbers))
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""

# for char in password_list:

#     password += char
# print(f"Your password is: {password}")


# Day 6
# Python Function & Karel
# To create our function by def
# def my_function():
    #Do this
    #Then Do This
    #Finally Do This


# def my_function():
#     print("Hello")
#     print("Bye")
#
# my_function()




# letters = ['a','b','c','d''e','f','g','s']
# length = len(letters)
# print(length)

# replace some values
# letters[2:5] = ['C','D','E']
# print(letters)

# now remove them
# letters[2:5] = []
# print(letters)

# Clear the list by replacing all the element with an empty list

# letters[:] = []
# print(letters)

# Nest List
# a = ['a','b','c']
# n = [1,2,3]
# x = [a,n]
# print(x)
# print(x[0])
# print(x[0][1])



# Fibonacci Series
# the sum of two elements defines the next

# a,b = 0,1
# while a < 10:
#     print(a)
#     a,b = b, a+b

# a, b  = 0,1
# while a < 1000:
#     print(a,end=',')
#     a,b = b, a+b




# Day 7 Hangman Game
#
# import random
#
# from hangman_word import word_list
# from hangman_art import HANGMAN_PICS,logo
#
#
# lives = 6
#
# print(logo)
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)
#
# game_over = False
# correct_letter = []
#
#
# while not game_over:
#     print(f"************************************************{lives}/6 LIVES LEFT************************")
#     guess = input("Guess a letter: ").lower()
#
#
# if guess in correct_letter:
#     print(f"You've already guessed{guess}")
#
#
#     display = ""
#
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letter.append(guess)
#         elif letter in correct_letter:
#             display += letter
#         else:
#             display += "_"
#
#
#     print("Word to guess: " + display)
#
#
#
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You Guessed {guess}, that's not in the word. You lose a life.")
#         if lives == 0:
#             game_over = True
#
#             print(f"******************************************** IT WAS {chosen_word}You Lose*********************************")
#
#     if "_"not in display:
#         game_over = True
#         print("*************************************You Win**************************************")
#
#     print(HANGMAN_PICS[lives])






# import random
# from hangman_word import word_list
# from hangman_art import HANGMAN_PICS, logo
#
# lives = 6
# print(logo)

# Select a random word
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# Placeholder to show progress
# placeholder = "_" * word_length
# print(f"Word to guess: {placeholder}")
#
# game_over = False
# correct_letter = []
#
# while not game_over:
#     print(f"************************************************ {lives}/6 LIVES LEFT ************************")
#     guess = input("Guess a letter: ").lower()
#
#     # Check if letter was already guessed
#     if guess in correct_letter:
#         print(f"You've already guessed {guess}. Try a different letter.")
#         continue
#
#     # Update the placeholder with correct guesses
#     display = ""
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display += letter
#             correct_letter.append(guess)
#         elif letter in correct_letter:
#             display += letter
#         else:
#             display += "_"
#
#     placeholder = display
#     print(f"Word to guess: {placeholder}")
#
#     # Decrease lives for incorrect guesses
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed '{guess}', that's not in the word. You lose a life.")
#         if lives == 0:
#             game_over = True
#             print(f"******************************************** IT WAS {chosen_word} - YOU LOSE *********************************")
#
#     # Check if player has won
#     if "_" not in placeholder:
#         game_over = True
#         print("************************************* YOU WIN **************************************")
#
#     # Display hangman art
#     print(HANGMAN_PICS[6 - lives])



# DAY 8 Fuctions with inputs
# Arguments & Parameters

# def greet():
#     print("Hello Angela")
#     print("How do you do Jack Bauer")
#     print("Isn't the weather nice?")

# greet()

# Function that allows fot inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Angel")
#
#
# def life_in_week(age):
#     years_left = 90 - age
#     weeks_left = years_left * 52
#     print(f"You have {weeks_left} weeks left.")
#
# age = int(input("Enter Your age: "))
# life_in_week(age)


# Functions with more than one input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
# greet_with("Jack Bauer", "Nowhere")

# greet_with(name = "Angela", location="London")

# def calculate_love_score(name1, name2):
#     combined_name = (name1 + name2).lower()
#
#     true_count = sum(combined_name.count(letter) for letter in "true")
#     love_count = sum(combined_name.count(letter) for letter in "love")
#
#     love_score = int(f"{true_count}{love_count}")
#
#     print(love_score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")









# Ceasar Cipher

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
#
# def caesar(original_text, shift_amount,encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount *= -1
#
#     for letter in original_text:
#         if letter not in alphabets:
#             output_text += letter
#         else:
#             shifted_position = alphabets.index(letter) + shift_amount # 7 -> 9
#             shifted_position %= len(alphabets)
#             output_text += alphabets[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
#
# should_continue = True
#
# while should_continue:
#
#     direction = input("Type 'encode' to encrypt type decode to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the Shift Number:\n"))
#
#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#
#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye")


























# Day 9
# Dictionaries & Nesting

# Dictionary {key: Value}


# programming_dictionaries = {
#     "Bug": "An error in a program that prevent the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again"
# }
# print(programming_dictionaries["Function"])
#
# programming_dictionaries["Loop"] = "The action of doing something over and over again"
#
# # Creating Empty Dictionarie
# empty_dictionary = {}
#
#
# # Wipe an existing Dictionarie
# # programming_dictionaries = {}
#
# # Edit an item in a dictionary
# programming_dictionaries["Bug"] = "A moth in your computer"
#
#
#
# # Loop through a dictionary
# # for thing in programming_dictionaries:
# #     print(thing)
# for key in programming_dictionaries:
#     print(key)
#     print(programming_dictionaries)




# Gradding Program
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
#
# for student, score in student_scores.items():
#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)


# Nesting
# {
#     key: Value,
#     key2: Value,
#       key: [List],
#       key2: [Dict]
# }


# capitals = {
#     "France ": "paris",
#     "German": "Berlin",
# }
# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
#
# print(travel_log["France"])
#
# nested_list = ["A", "B",["C","D"]]
#
# print(nested_list[2][1])
#
# travel_log = {
#     "France":
#         {
#     "cities_visited": 8,
#     "total_visited": ["Paris", "Lille", "Djon"]
#         },
#     "Germany": {
#     "cities_visited": ["Stuttgart", "Berlin", "Stuttgart"],
#     "total_visits": 5
# },
# }
# print(travel_log["Germany"])









# Secret Auction
# Todo : Compare bid in Dictionary

# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f'THe Winner is {winner} with a bid of ${highest_bid}.')
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#
#     elif should_continue == "yes":
#         print("\n" * 20)




















