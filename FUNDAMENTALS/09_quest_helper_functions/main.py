# 09 Quest Helper Functions
# This program teaches functions in Python.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# A function is a reusable block of code.
# We use functions when we want to organise code
# or avoid writing the same code again and again.

# def means "define a function".
# This function prints a welcome message.

def show_welcome_message():
    print("QUEST HELPER")
    print("------------")
    print("Welcome, adventurer!")
    print("This program will help check your quest progress.")


# A function does not run until we call it.
# Calling a function means typing its name with brackets.

show_welcome_message()


print()


# This function has a parameter.
# A parameter is information we give to a function.
# In this function, player_name is the parameter.

def greet_player(player_name):
    print(f"Hello, {player_name}!")
    print("Your quest is ready.")


# Ask the user for their name.

name = input("What is your player name? ")


# Now we call the function and give it the user's name.

greet_player(name)


print()


# This function checks quest progress.
# It uses if, elif, and else inside a function.

def check_quest_progress(quests_complete):
    if quests_complete >= 5:
        print("Quest Rank: Legend")
        print("You have completed heaps of quests!")
    elif quests_complete >= 3:
        print("Quest Rank: Explorer")
        print("You are making solid progress.")
    else:
        print("Quest Rank: Beginner")
        print("Keep going. Every quest counts.")


# input() gives us text first.
# int() changes the text into a whole number.

completed_quests = int(input("How many quests have you completed? "))


# Call the function and give it the number of completed quests.

check_quest_progress(completed_quests)


print()


# This function returns a value.
# return sends an answer back from the function.

def calculate_coins(quests_complete):
    coins = quests_complete * 10
    return coins


# Store the returned value in a variable.

earned_coins = calculate_coins(completed_quests)


# Print the result.

print("REWARD")
print("------")
print(f"You earned {earned_coins} coins.")


print()


# This final message reminds us why functions are useful.

print("Functions help us organise code into reusable chunks.")
print("Instead of writing everything in one big block, we can split code into smaller pieces.")