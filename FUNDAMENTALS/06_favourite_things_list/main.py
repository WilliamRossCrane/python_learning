# 06 Favourite Things List
# This program teaches lists in Python.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# A list stores more than one value.
# Lists use square brackets: [ ]

favourite_games = ["Pokemon", "Minecraft", "Mario Kart"]


# Each item in a list is separated by a comma.

favourite_foods = ["pizza", "sushi", "tacos"]


# print() can show the whole list.

print("FAVOURITE GAMES")
print("----------------")
print(favourite_games)


# An empty print() makes a blank line.
# This makes the terminal output easier to read.

print()


print("FAVOURITE FOODS")
print("----------------")
print(favourite_foods)


# Python starts counting from 0.
# This means the first item is at position 0.

print()
print("FIRST ITEMS")
print("-----------")

print(f"My first favourite game is {favourite_games[0]}.")
print(f"My first favourite food is {favourite_foods[0]}.")


# We can also get other items from the list.
# Position 1 means the second item.
# Position 2 means the third item.

print()
print("OTHER ITEMS")
print("-----------")

print(f"The second game in the list is {favourite_games[1]}.")
print(f"The third food in the list is {favourite_foods[2]}.")


# len() tells us how many items are in a list.
# len means length.

print()
print("LIST LENGTH")
print("-----------")

print(f"There are {len(favourite_games)} games in the games list.")
print(f"There are {len(favourite_foods)} foods in the foods list.")


# append() adds a new item to the end of a list.

favourite_games.append("Zelda")
favourite_foods.append("burgers")


# Now we print the updated lists.

print()
print("UPDATED LISTS")
print("-------------")

print(favourite_games)
print(favourite_foods)


# Lists are useful because real programs often need to store many things.

print()
print("Lists are useful for playlists, shopping carts, game items, and class rolls.")