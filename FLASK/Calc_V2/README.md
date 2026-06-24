# Calculator V2 — Database + Web + History 🧮

A simple Flask calculator web app that multiplies two numbers, saves the answer to a database, and shows previous calculations on a history page.

## About

This project is a beginner-friendly Flask app that shows how a small web app can connect to a database.

The app is similar to a basic calculator, but instead of only showing the answer, it also saves each calculation so it can be viewed later.

This project is useful for learning how websites can collect information, process it with Python, save it, and display it again.

## What the App Does

The app lets a user:

- Enter a first number
- Enter a second number
- Multiply the two numbers
- Save the result to a database
- View previous calculations on a history page

Example:

```text
5 x 4 = 20
```

## What I’m Learning

- Creating a Flask web app
- Using routes
- Using HTML templates
- Creating a form
- Reading form data
- Doing a calculation with Python
- Saving data to a database
- Showing saved data on a webpage
- Using Flask-SQLAlchemy
- Using Flask-Migrate
- Keeping a project organised

## Project Pages

The app has two main pages:

```text
/               Calculator page
/calculations   History page
```

## How the App Works

The app follows a simple flow:

```text
HTML form → Flask route → Python calculation → Database → History page
```

In simple words:

1. The user enters two numbers
2. The form sends the numbers to Flask
3. Flask multiplies the numbers
4. Flask saves the result to the database
5. The history page shows the saved calculations

## Main Files

```text
simpleCalc.py                    Starts the app
config.py                        Stores database settings
app/__init__.py                  Creates the Flask app and database connection
app/routes.py                    Controls the pages and calculator logic
app/models.py                    Creates the database table
app/forms.py                     Creates the form fields
app/templates/base.html          Main page layout
app/templates/index.html         Calculator page
app/templates/calculations.html  History page
app/static/style.css             Styling
```

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/CALCULATOR_V2_DB+WEB+HISTORY
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

## Step 3 — Install the Packages 📦

Install the packages needed for the project:

```bash
pip install -r requirements.txt
```

This installs Flask and the database tools.

## Step 4 — Create the Database 🗃️

Before the app can save calculations, the database needs to be set up.

Run:

```bash
flask --app simpleCalc db upgrade
```

This creates the database table.

Tip: if the history page is not working, try running this command again.

## Step 5 — Run the App 🚀

Start the Flask app:

```bash
flask --app simpleCalc run --debug
```

Open this link in the browser:

```text
http://127.0.0.1:5000
```

The `--debug` part is useful while learning because it helps show errors clearly.

## Step 6 — Test the Calculator ✅

Try entering:

```text
5
4
```

The answer should be:

```text
20
```

This means the calculator is working.

## Step 7 — Check the History Page 📋

Open:

```text
http://127.0.0.1:5000/calculations
```

You should see the saved calculation.

Example:

```text
5 | 4 | 20
```

This means the database is working.

## Step 8 — Stop the App 🛑

To stop the Flask app, go back to the terminal and press:

```text
control + c
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

Install the requirements again:

```bash
pip install -r requirements.txt
```

### Database Is Not Working

Run:

```bash
flask --app simpleCalc db upgrade
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
- [ ] Install the packages
- [ ] Add the Flask app files
- [ ] Add the database model
- [ ] Add the routes
- [ ] Add the HTML templates
- [ ] Add the CSS
- [ ] Run the database upgrade
- [ ] Start the app
- [ ] Test the calculator
- [ ] Test the history page

### Acknowledgement

Special thanks to Dan for allowing me to use and adapt these projects as part of my learning and future teaching.

These projects have helped me practise Flask, understand web app structure, and create beginner-friendly examples I can use with students.
