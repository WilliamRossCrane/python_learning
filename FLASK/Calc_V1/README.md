# Calculator Web 🧮

A simple Flask calculator website for learning how routes, templates, forms, and basic Python logic work together.

### About

This is a beginner-friendly Flask project.

It is designed as a first web app to help students understand how Flask connects Python code to webpages.

The app lets a user type in two numbers, choose a maths operation, and see the result on the page.

This project is useful for learning the basics of:

- Flask
- Routes
- HTML templates
- Forms
- Reading user input
- Simple Python calculations
- Styling a page with CSS

## What the App Does

The calculator lets a user:

- Enter a first number
- Enter a second number
- Choose an operation
- Calculate the answer
- Display the result on the page

The calculator can:

- Add
- Subtract
- Multiply
- Divide

Example:

```text
10 + 5 = 15
```

## What I’m Learning

- Creating a simple Flask app
- Making routes with `@app.route`
- Returning HTML pages with `render_template`
- Using a form to collect user input
- Reading form data with `request.form`
- Using `if`, `elif`, and `else` statements
- Displaying Python results in HTML
- Organising a small Flask project

## Project Page

The app has one main page:

```text
/    Calculator page
```

The form sends the calculator data to:

```text
/calculate
```

## How the App Works

The app follows a simple flow:

```text
HTML form → Flask route → Python calculation → Result shown on page
```

In simple words:

1. The user enters two numbers
2. The user chooses an operation
3. The form sends the data to Flask
4. Flask reads the numbers and operation
5. Flask does the calculation
6. The result is shown on the webpage

## Main Files

```text
simpleCalc.py             Starts the app
app/__init__.py           Creates the Flask app
app/routes.py             Controls the routes and calculator logic
app/templates/base.html   Main page layout
app/templates/index.html  Calculator form page
app/static/style.css      Styling
```

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/CALCULATOR_WEB
```

Tip: most commands need to be run from inside the project folder.

## Step 2 — Create a Virtual Environment 🧪

A virtual environment keeps this project’s Python packages separate from other projects.

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

If it worked, you should see this in the terminal:

```text
(venv)
```

## Step 3 — Install Flask 📦

Install Flask:

```bash
pip install flask
```

Save the package list:

```bash
pip freeze > requirements.txt
```

Tip: `requirements.txt` helps other people install the same packages later.

## Step 4 — Run the App 🚀

Start the Flask app:

```bash
flask --app simpleCalc run --debug
```

Open this link in the browser:

```text
http://127.0.0.1:5000
```

The `--debug` part is useful while learning because it helps show errors clearly.

## Step 5 — Test the Calculator ✅

Try entering:

```text
10
5
```

Then choose:

```text
Add
```

The answer should be:

```text
15
```

Try the other operations too:

```text
Subtract
Multiply
Divide
```

## Step 6 — Stop the App 🛑

To stop the Flask app, go back to the terminal and press:

```text
control + c
```

## Key Flask Ideas

## Routes

Routes are the URLs/pages in the app.

Example:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

This means:

```text
When the user visits /, show index.html
```

## Templates

Templates are HTML files.

Flask uses templates to show webpages to the user.

Example:

```python
return render_template("index.html")
```

## Forms

Forms let the user type information into the webpage.

In this app, the form collects:

- First number
- Second number
- Operation

## request.form

`request.form` is how Flask reads data from a submitted form.

Example:

```python
num1 = request.form["num1"]
```

This means:

```text
Get the value typed into the input named num1
```

## Common Problems 🛠️

### Flask Command Not Found

Make sure the virtual environment is active:

```bash
source venv/bin/activate
```

Then try running the app again:

```bash
flask --app simpleCalc run --debug
```

### A Package Is Missing

Install Flask again:

```bash
pip install flask
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### The Page Will Not Load

Make sure the app is running:

```bash
flask --app simpleCalc run --debug
```

Then open:

```text
http://127.0.0.1:5000
```

### The Calculator Does Not Work

Check that:

- The form uses `method="POST"`
- The form action goes to `/calculate`
- The input names match the Python code
- `routes.py` imports `request`
- The calculate route allows `methods=["POST"]`

## Important GitHub Note ⚠️

Do not upload the `venv` folder to GitHub.

The `venv` folder belongs to your own computer and can be recreated later.

Other people can recreate it by running:

```bash
python3 -m venv venv
pip install -r requirements.txt
```

Upload the code and `requirements.txt`, not the virtual environment.

## Build Checklist

Use this checklist when recreating the project:

- [ ] Create the project folder
- [ ] Create a virtual environment
- [ ] Install Flask
- [ ] Create the Flask app
- [ ] Add the home route
- [ ] Add the base template
- [ ] Add the calculator form
- [ ] Add the calculate route
- [ ] Read form data with `request.form`
- [ ] Add the maths logic
- [ ] Display the result on the page
- [ ] Add CSS styling
- [ ] Start the app
- [ ] Test add
- [ ] Test subtract
- [ ] Test multiply
- [ ] Test divide

## Acknowledgement

Special thanks to Dan for allowing me to use and adapt these projects as part of my learning and future teaching.

These projects have helped me practise Flask, understand web app structure, and create beginner-friendly examples I can use with students.
