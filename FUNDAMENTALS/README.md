# Python Fundamentals

Welcome to **Python Fundamentals**.

This is where we learn Python from the very beginning.

No huge apps yet.  
No confusing setup yet.  
No pretending we are hackers in a movie smashing the keyboard while green code flies everywhere.

Just simple Python programs that help you understand how coding actually works.

---

## Why Learn Python?

Python is one of the best programming languages for beginners because it is clear, readable, and used in the real world.

Python is used for things like:

- websites
- apps
- games
- data analysis
- artificial intelligence
- automation
- science
- robotics
- cybersecurity
- school projects
- tools that save people time

Python is not just a “school language”.

It is used by real companies, engineers, scientists, developers, and researchers.

---

## Python In Real Life

Python can be used behind the scenes in places students may already know.

### Netflix

Netflix has used Python for behind-the-scenes systems such as data tools, automation, infrastructure, and helping manage the huge technical systems involved in streaming.

When you open Netflix, Python is not the video you see on the screen.

It is more like one of the tools helping people and systems behind the scenes.

Python can help with questions like:

```text
What shows are popular?
What content should be recommended?
How do we monitor systems?
How do we keep huge services running smoothly?
```

That is real-world problem solving.

---

### Instagram

Instagram has used Python and Django for parts of its backend systems.

A backend is the part of an app users do not usually see.

When you like a photo, follow someone, refresh your feed, or open a profile, there are systems behind the screen making that happen.

Python can help build systems that deal with:

```text
users
posts
comments
likes
notifications
feeds
settings
```

That means Python is not just about printing “Hello”.

The same basics you learn here can grow into real app ideas later.

---

### NASA And Science

Python is also used in science and space-related projects.

Scientists and researchers use Python because it is great for working with data.

Python can help people:

```text
study space
analyse images
work with huge data sets
make graphs
run calculations
test ideas
build research tools
```

So yes, the same language we start with using `print()` can also be used for serious science.

Pretty cool.

---

## The Big Idea

Coding is giving instructions to a computer.

The computer is powerful, but it is also very literal.

If your instructions are clear, it follows them.

If your instructions are confusing, it gives an error.

That does not mean you failed.

It means the computer needs clearer instructions.

Coding is really just this cycle:

```text
write code
run code
read what happened
fix mistakes
try again
improve it
```

That is the whole game.

---

## How To Run A Python Program

Most beginner Python projects have a file called:

```text
main.py
```

To run it, open the terminal inside the project folder and type:

```bash
python3 main.py
```

This means:

```text
Use Python 3 to run the file called main.py
```

If the program works, you will see output in the terminal.

If the program does not work, you will see an error message.

Error messages are not the enemy.

They are clues.

---

## Your First Python Line

```python
print("Hello, Python!")
```

This tells Python to show a message in the terminal.

The message goes inside quotation marks because it is text.

In Python, text is called a **string**.

---

## Comments

Comments are notes for humans.

Python ignores comments when the program runs.

```python
# This is a comment.
# It explains the code below.

print("This line will run.")
```

Comments are useful because code can get confusing later.

Future you will appreciate past you explaining things clearly.

---

## Print Statements

`print()` displays something in the terminal.

```python
print("Welcome to Python.")
print("Coding is just problem solving.")
print("Small steps are better than giant confusing steps.")
```

Every `print()` statement appears on a new line.

Real-life connection:

```text
A game might print your score.
A quiz might print your result.
A program might print a warning message.
A school app might print a student report.
```

---

## Strings

A string is text.

Strings go inside quotation marks.

```python
name = "Alex"
message = "Welcome to coding!"
favourite_game = "Minecraft"
```

You can print strings:

```python
print(name)
print(message)
print(favourite_game)
```

Real-life connection:

```text
Your username is a string.
A movie title is a string.
A message in a chat app is a string.
A song name in Spotify is a string.
```

---

## Variables

A variable stores information.

Think of a variable like a labelled box.

```python
name = "Mia"
age = 13
year_level = 8
```

The variable name is on the left.

The value is on the right.

```python
print(name)
print(age)
print(year_level)
```

Real-life connection:

```text
A game uses variables for health, score, lives, and coins.
A shopping app uses variables for price, quantity, and total.
A school system uses variables for names, grades, and classes.
```

Variables are everywhere.

---

## Numbers

Python can work with numbers.

An **integer** is a whole number.

```python
score = 10
lives = 3
students = 25
```

A **float** is a decimal number.

```python
price = 4.50
height = 1.65
temperature = 23.7
```

Python can do maths:

```python
print(5 + 2)
print(10 - 3)
print(4 * 2)
print(8 / 2)
```

Maths symbols in Python:

```text
+   add
-   subtract
*   multiply
/   divide
```

Real-life connection:

```text
A game calculates your final score.
A shop calculates your total price.
A fitness app calculates distance and time.
A banking app calculates money.
```

---

## Booleans

A boolean is either:

```python
True
```

or:

```python
False
```

Booleans are used when a program needs to make decisions.

```python
is_raining = True
has_homework = False
game_over = False
```

Important: Python uses capital letters for booleans.

This works:

```python
True
False
```

This does not work:

```python
true
false
```

Python is picky like that.

Real-life connection:

```text
Is the user logged in?
Is the game over?
Is the password correct?
Is the video playing?
Is the item in stock?
```

Those are all true-or-false questions.

---

## Input

`input()` lets the user type something into the program.

```python
name = input("What is your name? ")

print("Hello, " + name)
```

This makes a program interactive.

Instead of only showing information, the program can ask questions and respond.

Real-life connection:

```text
A login form asks for your username.
A game asks for your character name.
A quiz asks for your answer.
A calculator asks for numbers.
```

---

## Basic Maths With Input

Input starts as text.

So if we want to use it as a number, we need to convert it.

```python
age = input("How old are you? ")

age = int(age)

print(age + 1)
```

If the user types:

```text
13
```

The output will be:

```text
14
```

`int()` changes the input into an integer.

That means Python can use it for maths.

---

## If Statements

An `if` statement lets a program make a decision.

```python
age = 13

if age >= 13:
    print("You are a teenager.")
else:
    print("You are not a teenager yet.")
```

The program checks a condition.

If the condition is true, one part runs.

If it is false, another part runs.

Real-life connection:

```text
If the password is correct, log the user in.
If the score is high enough, unlock the next level.
If the cart is empty, show a warning.
If the user is under 13, block certain features.
```

This is how programs start to feel smart.

---

## Elif

`elif` means:

```text
otherwise, if this other thing is true
```

Example:

```python
score = 75

if score >= 90:
    print("Excellent!")
elif score >= 50:
    print("You passed.")
else:
    print("Try again next time.")
```

Python checks from top to bottom.

Once it finds a true condition, it runs that block.

---

## Comparison Operators

Comparison operators compare values.

```text
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
```

Example:

```python
password = "dragon"

if password == "dragon":
    print("Access granted.")
else:
    print("Access denied.")
```

Important:

```python
=
```

means assign a value.

```python
==
```

means check if two things are equal.

They are not the same thing.

Classic beginner trap.

---

## Lists

A list stores multiple items.

```python
games = ["Minecraft", "Roblox", "Pokemon", "Mario Kart"]
```

You can print the whole list:

```python
print(games)
```

You can also print one item:

```python
print(games[0])
```

Python starts counting from `0`.

So:

```text
0 = first item
1 = second item
2 = third item
```

Real-life connection:

```text
A playlist is a list of songs.
A streaming app has a list of movies.
A game has a list of players.
A class roll is a list of students.
A shopping cart is a list of items.
```

Silly that it starts at zero? Yes.

Common in programming? Also yes.

---

## Loops

A loop repeats code.

This is useful when we do not want to write the same thing again and again.

```python
games = ["Minecraft", "Roblox", "Pokemon"]

for game in games:
    print(game)
```

This prints each game in the list.

Real-life connection:

```text
A music app loops through songs in a playlist.
A game loops through enemies on the screen.
A school system loops through student names.
An app loops through notifications.
```

Loops are one of the first things that make coding feel powerful.

---

## Dictionaries

A dictionary stores information using labels.

```python
student = {
    "name": "Sam",
    "age": 14,
    "year_level": 8
}
```

You can access information using the label:

```python
print(student["name"])
print(student["age"])
```

Real-life connection:

```text
A user profile is like a dictionary.
A Pokemon card could be stored like a dictionary.
A product in a shop could be stored like a dictionary.
A student record could be stored like a dictionary.
```

Example:

```python
pokemon = {
    "name": "Pikachu",
    "type": "Electric",
    "level": 25
}

print(pokemon["name"])
print(pokemon["type"])
print(pokemon["level"])
```

Dictionaries are useful when different pieces of information belong together.

---

## Functions

A function is a reusable block of code.

```python
def say_hello():
    print("Hello!")
    print("Welcome to Python.")

say_hello()
```

The function is created with:

```python
def
```

The function only runs when we call it:

```python
say_hello()
```

Real-life connection:

```text
A game might have a function to start a level.
A website might have a function to check a password.
A calculator might have a function to add numbers.
A music app might have a function to play a song.
```

Functions help us organise code and avoid repeating ourselves.

---

## Errors Are Normal

Errors are part of coding.

Even professional programmers get errors.

An error means:

```text
Python found something it does not understand.
```

When you get an error:

```text
1. Read the error slowly.
2. Check the line number.
3. Look for missing brackets.
4. Look for missing quotation marks.
5. Check spelling.
6. Fix one thing.
7. Run the program again.
```

The best coders are not perfect.

They are just good at debugging.

---

## Common Beginner Mistakes

Missing quotation marks:

```python
print(Hello)
```

Correct version:

```python
print("Hello")
```

Missing brackets:

```python
print("Hello"
```

Correct version:

```python
print("Hello")
```

Using lowercase booleans:

```python
is_ready = true
```

Correct version:

```python
is_ready = True
```

Using `=` instead of `==`:

```python
if password = "dragon":
    print("Correct")
```

Correct version:

```python
if password == "dragon":
    print("Correct")
```

Mistakes like this are normal.

Spotting them is a skill.

---

## Cool Things You Will Be Able To Build

By learning these basics, you can start building mini programs like:

```text
name generators
quiz games
score trackers
simple calculators
random choice games
password checkers
daily mood checkers
mini adventure games
shopping list programs
student grade checkers
file-saving note apps
basic data trackers
terminal games
```

Small programs teach big ideas.

---

## How To Think Like A Programmer

When building a program, ask:

```text
What should the program do?
What information does it need?
What should happen first?
What should happen next?
What decisions does it need to make?
What could go wrong?
How can I test it?
```

Programming is not just typing code.

Programming is thinking clearly.

---

## Tiny Challenges

Try these when learning.

### Challenge 1

Print your name, age, and favourite game.

### Challenge 2

Create variables for your name, favourite subject, and favourite food.

### Challenge 3

Ask the user for their name and say hello to them.

### Challenge 4

Ask the user for their age and tell them how old they will be next year.

### Challenge 5

Create a list of three favourite movies, games, or songs and print each one.

### Challenge 6

Make a simple password checker.

### Challenge 7

Make a quiz with one question.

### Challenge 8

Make a program that gives different messages depending on the user’s score.

---

## Reflection Questions

After each project, ask:

```text
What did this program do?
What new Python idea did I learn?
What part confused me?
What error did I fix?
What would I change next time?
How could I make this more fun?
```

Reflection helps you become a better coder.

Not just someone who copied code.

---

## The Main Rule

Do not try to learn everything at once.

Learn one idea.

Run it.

Break it.

Fix it.

Change it.

Run it again.

That is coding.
