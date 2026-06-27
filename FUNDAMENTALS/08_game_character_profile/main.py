# 08 Game Character Profile
# This program teaches dictionaries in Python.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# A dictionary stores information using labels.
# The labels are called keys.
# The information is called values.

# This dictionary stores information about a game character.

character = {
    "name": "Blaze",
    "class": "Fire Mage",
    "level": 5,
    "health": 80,
    "special_move": "Flame Burst"
}


# Each key is on the left.
# Each value is on the right.

# Example:
# "name" is a key.
# "Blaze" is the value.


print("GAME CHARACTER PROFILE")
print("----------------------")


# We can get information from a dictionary using its key.

print(f"Name: {character['name']}")
print(f"Class: {character['class']}")
print(f"Level: {character['level']}")
print(f"Health: {character['health']}")
print(f"Special Move: {character['special_move']}")


# Dictionaries are useful because related information can stay together.

print()
print("CHARACTER UPDATE")
print("----------------")


# We can update a value in a dictionary.
# This changes the level from 5 to 6.

character["level"] = 6


# We can also update the health.

character["health"] = 95


print(f"{character['name']} levelled up!")
print(f"New Level: {character['level']}")
print(f"New Health: {character['health']}")


print()
print("FULL CHARACTER DATA")
print("-------------------")


# We can loop through a dictionary.
# This lets us print every key and value.

for key in character:
    print(f"{key}: {character[key]}")


print()
print("Dictionaries are useful for storing profiles, game stats, products, and settings.")