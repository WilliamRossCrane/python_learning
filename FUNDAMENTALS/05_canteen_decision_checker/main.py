# 05 Canteen Decision Checker
# This program uses maths and if statements to make a decision.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# input() lets the user type an answer.
# input() always gives us text first.

student_name = input("What is your name? ")


# float() changes text into a decimal number.
# We use float for money because money can have cents.

budget = float(input("How much money do you have? $"))

item_name = input("What item do you want to buy? ")

item_price = float(input("How much does one item cost? $"))


# int() changes text into a whole number.
# We use int for quantity because we usually buy a whole number of items.

quantity = int(input("How many do you want to buy? "))


# This calculates the total cost.
# The * symbol means multiply.

total_cost = item_price * quantity


# This calculates how much money is left after buying the items.

money_left = budget - total_cost


# Print a simple summary first.

print()
print("CANTEEN CHECK")
print("-------------")

print(f"Student: {student_name}")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost}")
print(f"Budget: ${budget}")
print(f"Money Left: ${money_left}")


# Now the program makes a decision.
# An if statement checks if something is true.

print()
print("DECISION")
print("--------")


# If money_left is greater than 0, the student can afford it and has money left.

if money_left > 0:
    print(f"Good news, {student_name}!")
    print(f"You can buy the {item_name} and still have money left.")


# elif means "otherwise, if this other condition is true".
# If money_left is exactly 0, the student can afford it but will have no money left.

elif money_left == 0:
    print(f"You can buy the {item_name}, {student_name}.")
    print("But you will have no money left after buying it.")


# else runs if none of the conditions above were true.
# If money_left is less than 0, the student does not have enough money.

else:
    print(f"Sorry, {student_name}.")
    print(f"You do not have enough money to buy the {item_name}.")


# This final message reminds us what the program learned.

print()
print("This program used if, elif, and else to make a decision.")