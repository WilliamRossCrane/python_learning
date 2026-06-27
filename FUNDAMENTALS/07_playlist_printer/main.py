# 07 Playlist Printer
# This program teaches for loops in Python.

# To run this program:
# 1. Open the terminal.
# 2. Move into this folder.
# 3. Type:
#    python3 main.py


# A list stores more than one value.
# This list stores song names.

playlist = ["Blinding Lights", "Anti-Hero", "Cruel Summer", "As It Was"]


# We could print each song one by one like this:

print("PRINTING SONGS WITHOUT A LOOP")
print("-----------------------------")

print(playlist[0])
print(playlist[1])
print(playlist[2])
print(playlist[3])


# That works, but it is repetitive.
# If the playlist had 100 songs, this would be annoying.
# A loop lets us repeat code without writing the same line again and again.

print()
print("PRINTING SONGS WITH A LOOP")
print("--------------------------")


# A for loop goes through each item in a list.
# song is a variable name we made up.
# Each time the loop runs, song becomes the next item in the playlist.

for song in playlist:
    print(song)


# The indented line belongs to the loop.
# Indentation means spaces at the start of a line.
# In Python, indentation is very important.


print()
print("NUMBERED PLAYLIST")
print("-----------------")


# We can use a counter to number the songs.
# This variable starts at 1 because humans usually count from 1.

song_number = 1


# This loop prints each song with a number.

for song in playlist:
    print(f"{song_number}. {song}")

    # This adds 1 to the song number.
    # It means the next song gets the next number.

    song_number = song_number + 1


print()
print("PLAYLIST SUMMARY")
print("----------------")


# len() tells us how many items are in a list.

print(f"This playlist has {len(playlist)} songs.")


# This final message connects loops to real programs.

print()
print("Loops are useful when programs need to repeat actions.")
print("Apps, games, websites, and music players use loops all the time.")