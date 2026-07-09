````markdown
# Python Fundamentals

This folder is for learning basic Python.

These projects use simple Python files like:

```text
main.py
```

No web apps.  
No servers.  
No extra packages.

Just beginner Python practice.

---

## What You Will Learn

These projects practise:

- `print()`
- comments
- variables
- strings
- numbers
- input
- if statements
- lists
- loops
- dictionaries
- functions
- debugging

---

## How Python Works

Python reads code from top to bottom.

Example:

```python
print("Hello")
print("Welcome to Python")
print("This line runs last")
```

Output:

```text
Hello
Welcome to Python
This line runs last
```

---

## Basic Syntax

### Print

`print()` shows something in the terminal.

```python
print("Hello, Python!")
```

---

### Comments

Comments explain code.

Python ignores comments when the program runs.

```python
# This is a comment.

print("This line runs.")
```

---

### Variables

Variables store information.

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

Python can use whole numbers and decimal numbers.

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

Use `int()` for whole numbers:

```python
age = int(input("How old are you? "))

print(age + 1)
```

Use `float()` for decimal numbers:

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

---

## Common Mistakes

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

`=` stores a value.  
`==` checks if two values are equal.

---

## Learning Rule

Learn one idea.

Run it.

Change it.

Break it.

Fix it.

Run it again.

That is coding.
````
