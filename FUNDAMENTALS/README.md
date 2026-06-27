````markdown
# Python Fundamentals

This folder is for learning the basics of Python.

The goal is simple:

- write small programs
- run them in the terminal
- read the output
- fix mistakes
- practise one idea at a time

Python is used for apps, games, websites, data, automation, AI, school projects, and tools that save time.

---

## How To Open The Terminal

In VS Code:

1. Open the project folder.
2. Click **Terminal** in the top menu.
3. Click **New Terminal**.

The terminal is where we run Python commands.

---

## How To Run A Python File

Most projects have a file called:

```text
main.py
```
````

To run it, use:

```bash
python3 main.py
```

Example:

```bash
cd FUNDAMENTALS/01_hello_python
python3 main.py
```

If it works, you will see output in the terminal.

If something is wrong, Python will show an error message.

Errors are normal. They help you find what to fix.

---

## Basic Python Syntax

### Print

`print()` shows something in the terminal.

```python
print("Hello, Python!")
```

---

### Comments

Comments are notes for humans.

Python ignores comments when the program runs.

```python
# This is a comment.

print("This line runs.")
```

---

### Variables

A variable stores information.

```python
name = "Alex"
age = 13

print(name)
print(age)
```

---

### Strings

A string is text.

Strings use quotation marks.

```python
subject = "Digital Technologies"

print(subject)
```

---

### Numbers

Python can use numbers.

```python
score = 10
price = 4.50

print(score)
print(price)
```

Basic maths:

```python
print(5 + 2)
print(10 - 3)
print(4 * 2)
print(8 / 2)
```

---

### Input

`input()` lets the user type into the program.

```python
name = input("What is your name? ")

print("Hello, " + name)
```

Input starts as text.

Use `int()` when you need a whole number.

```python
age = int(input("How old are you? "))

print(age + 1)
```

Use `float()` when you need a decimal number.

```python
price = float(input("Enter a price: "))

print(price)
```

---

### If Statements

`if` statements let a program make decisions.

```python
score = 75

if score >= 50:
    print("You passed.")
else:
    print("Try again.")
```

Use `elif` to check another condition.

```python
score = 90

if score >= 90:
    print("Excellent.")
elif score >= 50:
    print("You passed.")
else:
    print("Try again.")
```

---

### Comparison Operators

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

```text
=   stores a value
==  checks if two values are equal
```

---

### Lists

A list stores multiple items.

```python
games = ["Minecraft", "Pokemon", "Mario Kart"]

print(games)
print(games[0])
```

Python starts counting from `0`.

So `games[0]` means the first item.

---

### Loops

A loop repeats code.

```python
games = ["Minecraft", "Pokemon", "Mario Kart"]

for game in games:
    print(game)
```

This prints every item in the list.

---

### Dictionaries

A dictionary stores information using labels.

```python
student = {
    "name": "Sam",
    "age": 14,
    "year_level": 8
}

print(student["name"])
print(student["age"])
```

---

### Functions

A function is a reusable block of code.

```python
def say_hello():
    print("Hello!")
    print("Welcome to Python.")

say_hello()
```

Functions help keep code organised.

---

## Common Beginner Mistakes

Missing quotation marks:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

Missing bracket:

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

Using lowercase booleans:

```python
is_ready = true
```

Correct:

```python
is_ready = True
```

Using `=` instead of `==`:

```python
password = "dragon"

if password == "dragon":
    print("Access granted.")
```

---

## Debugging

Debugging means finding and fixing mistakes.

When something breaks:

1. Read the error message.
2. Check the line number.
3. Look for spelling mistakes.
4. Check brackets and quotation marks.
5. Fix one thing.
6. Run the program again.

---

## Learning Rule

Do not try to learn everything at once.

Learn one idea.

Run it.

Change it.

Break it.

Fix it.

Run it again.

That is coding.

```

```
