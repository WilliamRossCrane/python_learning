# 10 Bug Detective Debugging Lab
# This program teaches errors, debugging, and safe input.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# Bugs are mistakes in code.
# Debugging means finding and fixing those mistakes.

# Errors are normal.
# Even professional programmers get errors every day.


def show_title():
    print("BUG DETECTIVE DEBUGGING LAB")
    print("---------------------------")
    print("Your mission is to learn how to spot and fix bugs.")
    print()


show_title()


# Common beginner bugs are shown below.
# These broken examples are written as comments so they do not crash the program.


print("COMMON BEGINNER BUGS")
print("--------------------")


# Bug 1: Missing quotation marks
# Broken version:
# print(Hello)

# Fixed version:
print("Bug 1 fixed: Text needs quotation marks.")


# Bug 2: Missing closing bracket
# Broken version:
# print("Hello"

# Fixed version:
print("Bug 2 fixed: Brackets need to open and close.")


# Bug 3: Using a variable before it exists
# Broken version:
# print(score)

# Fixed version:
score = 10
print(f"Bug 3 fixed: The score is {score}.")


# Bug 4: Trying to do maths with text
# Broken version:
# age = input("How old are you? ")
# print(age + 1)

# Fixed version:
age = int("13")
print(f"Bug 4 fixed: 13 plus 1 is {age + 1}.")


print()


# Now we will make a small program that handles user input safely.

print("SAFE SCORE CHECKER")
print("------------------")


player_name = input("What is your name? ")

score_text = input("Enter your test score out of 100: ")


# input() always gives us text.
# int() tries to change the text into a whole number.
# But if the user types something like "hello", Python cannot turn that into a number.


# try means:
# Try to run this code.

try:
    score = int(score_text)

    print()
    print(f"Thanks, {player_name}. Your score was {score}.")

    if score >= 90:
        print("Result: Excellent work!")
    elif score >= 50:
        print("Result: You passed.")
    else:
        print("Result: Keep practising. You can improve.")


# except means:
# If there is a problem, run this code instead of crashing.

except ValueError:
    print()
    print("Oops! That was not a number.")
    print("Please run the program again and type a number like 75.")


print()


# Debugging tip:
# We can use print() to check what is happening inside a program.

print("DEBUGGING TIP")
print("-------------")
print("Use print() to check variable values while testing your code.")
print("Read error messages slowly. They usually tell you where the problem is.")


print()
print("Remember: bugs are clues, not failure.")