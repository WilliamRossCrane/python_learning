# 03 Interactive Profile Card
# This program asks the user questions and stores their answers.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# input() lets the user type something into the program.
# The question inside input() is called a prompt.
# A clear prompt helps the user know what to type.

student_name = input("What is your name? ")

year_level = input("What year level are you in? ")

favourite_subject = input("What is your favourite subject? ")

favourite_game = input("What is your favourite game? ")

learning_goal = input("What is one thing you want to get better at in Python? ")


# print() shows information in the terminal.
# An empty print() creates a blank line.
# Blank lines make the output easier to read.

print()
print("STUDENT PROFILE CARD")
print("--------------------")


# An f-string lets us put variables inside a string.
# To make an f-string, put the letter f before the quotation marks.
# Then place variable names inside curly brackets: { }

print(f"Name: {student_name}")
print(f"Year Level: {year_level}")
print(f"Favourite Subject: {favourite_subject}")
print(f"Favourite Game: {favourite_game}")
print(f"Python Goal: {learning_goal}")


# We can reuse the same variables again later in the program.
# This makes our code more useful and less repetitive.

print()
print(f"Welcome to Python, {student_name}!")
print(f"You are learning Python because you want to {learning_goal}.")
print("Small steps make big programs.")