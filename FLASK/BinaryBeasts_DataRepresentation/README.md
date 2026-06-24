# BinaryBeasts Data Representation 🐉💾

A beginner-friendly Flask web app that helps students learn how computers represent data.

BinaryBeasts teaches students that computers do not store information the same way humans understand it. Instead, computers use values, patterns, numbers, binary, pixels, and colour codes to represent information.

This project is designed for students learning beginner Flask, HTML, CSS, forms, routes, helper functions, and core Digital Technologies ideas.

---

## About the Project

BinaryBeasts is an interactive data representation learning app.

Students can use the app to explore how computers represent:

- Numbers
- Binary values
- Text
- Colours
- Pixels
- Simple digital images

The project includes several small tools that each teach one important idea.

---

## What the App Does

BinaryBeasts lets students:

- Convert decimal numbers to binary
- Convert binary values back to decimal
- Convert text into binary
- Create colours using RGB values
- Build a tiny pixel creature using colour data
- See how data can become something visual on a screen

---

## What Students Are Learning

This project teaches two types of skills.

### Coding Skills

Students practise:

- Creating a Flask web app
- Using routes
- Rendering HTML templates
- Using forms
- Handling POST requests
- Reading input from users
- Using helper functions
- Validating input
- Using dictionaries
- Using loops
- Passing data from Python into HTML
- Displaying results with Jinja
- Styling pages with CSS

### Digital Technologies Skills

Students learn:

- Computers use data to represent information
- Binary only uses `0` and `1`
- A bit is a single binary digit
- A byte is 8 bits
- Decimal numbers can be converted into binary
- Binary values can be converted back into decimal
- Text can be represented as numbers and binary
- Colours can be represented using RGB values
- Images are made from pixels
- Each pixel stores colour data

---

## Key Vocabulary

### Bit

A bit is a single binary digit.

It can only be:

```text
0 or 1
```

---

### Byte

A byte is a group of 8 bits.

Example:

```text
01000001
```

---

### Binary

Binary is a number system that only uses two digits:

```text
0 and 1
```

Computers use binary because electronic circuits can represent two states, such as on/off or true/false.

---

### Decimal

Decimal is the number system humans usually use.

It uses ten digits:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

### RGB

RGB stands for:

```text
Red
Green
Blue
```

Each colour value can be between:

```text
0 and 255
```

Example:

```text
rgb(255, 0, 0) = red
rgb(0, 255, 0) = green
rgb(0, 0, 255) = blue
```

---

### Pixel

A pixel is a tiny square of colour.

Digital images are made from many pixels.

Each pixel stores colour data.

---

## Main Pages

```text
/                    Home page
/binary-converter    Decimal to binary converter
/decimal-converter   Binary to decimal converter
/text-to-binary      Text to binary converter
/rgb-lab             RGB colour lab
/pixel-beast         Pixel beast activity
```

---

## Main Files

```text
binarybeasts.py                  Starts the Flask app
requirements.txt                 Python packages needed for the project
README.md                        Project instructions and explanation

app/__init__.py                  Creates the Flask app
app/routes.py                    Controls the routes and page logic
app/converters.py                Stores helper functions for conversions

app/templates/base.html          Shared layout used by every page
app/templates/index.html         Home page
app/templates/binary_converter.html
app/templates/decimal_converter.html
app/templates/text_to_binary.html
app/templates/rgb_lab.html
app/templates/pixel_beast.html

app/static/css/style.css         Styling for the app
```

---

## How the App Works

The app follows this basic flow:

```text
User enters data
        ↓
Flask receives the form
        ↓
Python processes the input
        ↓
A result is created
        ↓
Flask sends the result to HTML
        ↓
The browser displays the answer
```

This is called:

```text
Input → Process → Output
```

---

## Tool 1 — Decimal to Binary Converter

The decimal to binary converter lets students enter a normal number and see the binary version.

Example:

```text
Decimal: 13
Binary: 1101
```

This teaches that numbers can be represented in different number systems.

### Key Code Idea

```python
bin(decimal_number)[2:]
```

Example:

```python
bin(13)
```

returns:

```text
0b1101
```

The `[2:]` removes the `0b`, leaving:

```text
1101
```

---

## Tool 2 — Binary to Decimal Converter

The binary to decimal converter lets students enter a binary value and see the decimal version.

Example:

```text
Binary: 1010
Decimal: 10
```

This reinforces that binary patterns represent values.

### Key Code Idea

```python
int(binary_string, 2)
```

The `2` tells Python that the input is base 2, which means binary.

---

## Tool 3 — Text to Binary Converter

The text to binary converter lets students enter letters or words and see the binary representation.

Example:

```text
Text: A
Binary: 01000001
```

Example:

```text
Text: Cat
Binary: 01000011 01100001 01110100
```

This teaches that text can be stored as numbers, and those numbers can be represented in binary.

### Key Code Idea

```python
ord("A")
```

This gives:

```text
65
```

Then:

```python
format(65, "08b")
```

gives:

```text
01000001
```

---

## Tool 4 — RGB Colour Lab

The RGB colour lab lets students enter red, green, and blue values to create a colour.

Example:

```text
Red: 255
Green: 0
Blue: 0
Result: red
```

This teaches that colours on a screen are represented using numerical data.

### Key Code Idea

```python
rgb(255, 0, 0)
```

means:

```text
Full red
No green
No blue
```

The app also creates a hex colour code.

Example:

```text
#FF0000
```

---

## Tool 5 — Pixel Beast Activity

The Pixel Beast activity lets students change the colour of each pixel in a 3 by 3 grid.

Students can create a tiny pixel creature by choosing colours from dropdown menus.

This teaches that digital images are made from pixels, and each pixel stores colour data.

Example pixel data:

```text
Pixel 1: white = #F9FAFB
Pixel 2: green = #22C55E
Pixel 3: white = #F9FAFB
```

### Key Code Ideas

The project uses a dictionary to store colour names and hex values.

```python
PIXEL_COLOURS = {
    "black": "#111827",
    "white": "#F9FAFB",
    "green": "#22C55E",
    "blue": "#3B82F6",
    "purple": "#A855F7",
    "yellow": "#FACC15",
    "red": "#EF4444",
}
```

This lets the app connect a simple colour name to a real colour value.

---

## Key Coding Idea — Routes

Routes tell Flask what page to show.

Example:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

This means:

```text
When the user visits /
show index.html
```

Another example:

```python
@app.route("/rgb-lab", methods=["GET", "POST"])
def rgb_lab():
    return render_template("rgb_lab.html")
```

This means:

```text
When the user visits /rgb-lab
show the RGB lab page
```

---

## Key Coding Idea — GET and POST

This project uses both GET and POST requests.

### GET

GET is used when the user first opens a page.

Example:

```text
User visits /binary-converter
```

The page loads with an empty form.

---

### POST

POST is used when the user submits a form.

Example:

```text
User enters 13
User clicks Convert
Flask receives the submitted value
Python converts it to binary
The page displays 1101
```

---

## Key Coding Idea — Helper Functions

The project uses helper functions inside:

```text
app/converters.py
```

Helper functions keep the code organised.

Instead of putting all the logic inside `routes.py`, conversion code is separated into functions.

Example:

```python
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]
```

This makes the project easier to read, test, and teach.

---

## Key Coding Idea — Templates

Templates are HTML files used by Flask.

Example:

```python
return render_template("binary_converter.html")
```

This tells Flask to display:

```text
app/templates/binary_converter.html
```

Templates help separate:

```text
Python logic
HTML structure
CSS styling
```

---

## Key Coding Idea — Jinja

Jinja lets HTML display Python values.

Example:

```html
<strong>{{ binary_result }}</strong>
```

If Python sends:

```text
binary_result = 1101
```

Then the page displays:

```text
1101
```

Jinja also lets templates use loops.

Example:

```html
{% for pixel in pixel_grid %}
<li>{{ pixel.name }}</li>
{% endfor %}
```

---

## Key Coding Idea — Shared Layout

Every page extends `base.html`.

Example:

```html
{% extends "base.html" %}
```

This means every page shares the same:

- Header
- Navigation
- Main layout
- CSS link

This avoids repeating the same HTML in every file.

---

## Key Coding Idea — CSS Styling

The CSS file controls how the app looks.

The stylesheet is linked once in `base.html`.

```html
<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/style.css') }}"
/>
```

Because every page extends `base.html`, every page receives the same styling.

This is why the project does not need the CSS link repeated in every template.

---

## How to Start the Project

### Step 1 — Go Into the Project Folder

```bash
cd "/Users/william.c/Documents/Visual Studio Code/python_learning/FLASK/BinaryBeasts_DataRepresentation"
```

---

### Step 2 — Create a Virtual Environment

```bash
python3 -m venv venv
```

---

### Step 3 — Activate the Virtual Environment

```bash
source venv/bin/activate
```

You should see:

```text
(venv)
```

---

### Step 4 — Install the Requirements

```bash
pip install -r requirements.txt
```

---

### Step 5 — Run the App

```bash
flask --app binarybeasts:app run --debug
```

---

### Step 6 — Open the App

Open this in the browser:

```text
http://127.0.0.1:5000
```

---

### Step 7 — Stop the App

To stop the app, press:

```text
control + c
```

---

## Test Checklist

Use this checklist to make sure the project works.

- [ ] Home page loads
- [ ] Navigation links work
- [ ] Decimal to binary converter works
- [ ] Binary to decimal converter works
- [ ] Text to binary converter works
- [ ] RGB colour lab works
- [ ] Pixel Beast activity works
- [ ] Forms submit correctly
- [ ] Invalid inputs show errors
- [ ] CSS styling appears correctly

---

## Values to Test

### Decimal to Binary

```text
0   → 0
1   → 1
2   → 10
5   → 101
8   → 1000
13  → 1101
255 → 11111111
```

---

### Binary to Decimal

```text
0        → 0
1        → 1
10       → 2
101      → 5
1000     → 8
1101     → 13
11111111 → 255
```

Try an invalid value:

```text
102
```

This should show an error because binary can only contain `0` and `1`.

---

### Text to Binary

```text
A     → 01000001
B     → 01000010
Cat   → 01000011 01100001 01110100
Hello → 01001000 01100101 01101100 01101100 01101111
```

---

### RGB Lab

```text
255, 0, 0       → red
0, 255, 0       → green
0, 0, 255       → blue
255, 255, 0     → yellow
255, 255, 255   → white
0, 0, 0         → black
120, 80, 200    → purple-ish
```

---

### Pixel Beast

Test that:

- Dropdowns appear
- Pixel colours can be changed
- The 3 by 3 grid updates
- Pixel data updates underneath the grid

---

## Common Problems

### Flask Command Not Found

Make sure the virtual environment is active.

```bash
source venv/bin/activate
```

Then run:

```bash
flask --app binarybeasts:app run --debug
```

---

### Module Not Found

Install the requirements again.

```bash
pip install -r requirements.txt
```

---

### Page Not Found

Check that the route exists in:

```text
app/routes.py
```

Also check that the link uses the correct function name.

Example:

```html
<a href="{{ url_for('rgb_lab') }}">RGB Lab</a>
```

The route function must be named:

```python
def rgb_lab():
```

---

### Template Not Found

Check that the template exists inside:

```text
app/templates/
```

Example:

```text
rgb_lab.html
pixel_beast.html
```

Also check the spelling in `render_template`.

Example:

```python
return render_template("rgb_lab.html")
```

---

### CSS Not Showing

Check that `base.html` links to the stylesheet.

```html
<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/style.css') }}"
/>
```

Also check that the CSS file exists here:

```text
app/static/css/style.css
```

---

### Pixel Beast Template Error

If Jinja gives a template error, check the if statement inside the dropdown options.

A safe version is:

```html
{% if colour_name == pixel.name %}
<option value="{{ colour_name }}" selected>{{ colour_name.title() }}</option>
{% else %}
<option value="{{ colour_name }}">{{ colour_name.title() }}</option>
{% endif %}
```

---

## Important GitHub Note

Do not upload the `venv` folder to GitHub.

The virtual environment belongs to your computer and can be recreated later.

The `.gitignore` file should include:

```text
venv/
__pycache__/
*.pyc
*.pyo
.env
.DS_Store
```

Upload:

- Python files
- HTML templates
- CSS file
- README
- requirements.txt

Do not upload:

- venv folder
- cache files
- private environment files

---

## Build Checklist

This project was built step by step.

- [ ] Create project structure
- [ ] Add Flask app setup
- [ ] Add home page
- [ ] Add decimal to binary converter
- [ ] Add binary to decimal converter
- [ ] Add text to binary converter
- [ ] Add RGB colour lab
- [ ] Add Pixel Beast activity
- [ ] Add BinaryBeasts theme
- [ ] Add README documentation

---

## Suggested Commit Order

```text
chore: create binary beasts project structure
feat: add flask app setup
feat: add home page
feat: add decimal to binary converter
feat: add binary to decimal converter
feat: add text to binary converter
feat: add rgb colour lab
feat: add pixel beast activity
style: add binary beasts theme
docs: add binary beasts readme
```

Small commits make the project easier to understand because each commit teaches one clear idea.

---

## Extension Ideas

Students could extend this project by adding:

- Binary addition calculator
- Binary quiz
- ASCII table page
- Image compression explanation
- Larger pixel art grid
- Save a pixel beast design
- Random pixel beast generator
- RGB sliders instead of number inputs
- Hex to RGB converter
- Binary to text converter
- Score-based data quiz
- Student reflection page

---

## Challenge Ideas

### Beginner Challenge

Add a new route called:

```text
/bit-byte
```

Create a page that explains the difference between a bit and a byte.

---

### Intermediate Challenge

Add a binary quiz.

Example question:

```text
What is decimal 5 in binary?
```

Options:

```text
101
111
100
```

---

### Advanced Challenge

Create a 5 by 5 pixel grid instead of a 3 by 3 grid.

Think about:

- How many pixels are needed?
- How many form inputs are needed?
- How could a loop make this easier?

---

## Student Reflection Questions

After completing the project, students could answer:

1. What is a bit?
2. What is a byte?
3. Why do computers use binary?
4. How can a decimal number be converted into binary?
5. How can binary be converted back into decimal?
6. How can text be represented as numbers?
7. What does RGB stand for?
8. How are colours stored as data?
9. What is a pixel?
10. How are digital images made from pixels?
11. Why is input validation important?
12. How does Flask pass data from Python into HTML?
13. Why is it useful to keep helper functions in a separate file?
14. Why does every page extend `base.html`?
15. How could this app be improved?

---

## Why This Project Matters

BinaryBeasts shows students that data is behind almost everything they see on a computer.

A number can become binary.

A letter can become binary.

A colour can become three numbers.

An image can become a grid of pixels.

This project connects coding with real Digital Technologies concepts and helps students understand that computers represent the world using data.

---

## Acknowledgement

This project was created as a beginner-friendly Flask learning app for students exploring data representation, binary, text encoding, RGB colours, pixels, and basic web development.

It is designed to help students connect coding, creativity, and core computing concepts.
