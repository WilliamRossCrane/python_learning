# 04 Canteen Budget Calculator
# This program uses input, numbers, and basic maths.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# input() lets the user type an answer.
# Important beginner rule:
# input() always gives us text, even if the user types a number.

student_name = input("What is your name? ")


# A float is a number that can have decimals.
# Money often uses decimals, like 10.50 or 4.25.
# float() changes the user's text input into a decimal number.

budget = float(input("How much money do you have? $"))


# This is another float because item prices can have decimals.

item_price = float(input("How much does one item cost? $"))


# An integer is a whole number.
# Quantity should be a whole number, like 1, 2, or 3.
# int() changes the user's text input into a whole number.

quantity = int(input("How many items do you want to buy? "))


# Now we can do maths with the numbers.

total_cost = item_price * quantity

money_left = budget - total_cost


# Now we print a clear receipt for the user.

print()
print("CANTEEN BUDGET RECEIPT")
print("----------------------")


# f-strings let us place variables inside text.
# The variable goes inside curly brackets { }.

print(f"Student: {student_name}")
print(f"Budget: ${budget}")
print(f"Item Price: ${item_price}")
print(f"Quantity: {quantity}")


# We can also print the answers from our calculations.

print()
print(f"Total Cost: ${total_cost}")
print(f"Money Left: ${money_left}")


# This final message connects the code to real life.

print()
print("Python can help solve everyday problems, like working out money.")