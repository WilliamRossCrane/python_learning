# Porkies CRUD — Orders + Database + Web 🍖

A beginner-friendly Flask CRUD web app for managing Porkies BBQ customer orders.

This app lets a user create, view, edit, and delete customer orders. It also connects orders to delivery drivers and saves everything to a database.

## About

This project is a simple Flask web app that shows how a small business-style order system can work.

The app is based around Porkies BBQ Restaurant and demonstrates how a web app can collect information from a user, save it to a database, display it on a page, update it, and delete it.

This project is useful for learning how CRUD apps work.

CRUD stands for:

```text
Create
Read
Update
Delete
```

## What the App Does

The app lets a user:

- Create a new customer order
- View all saved orders
- Edit an existing order
- Delete an order
- Assign an order to a driver
- Track the order status
- View a simple order summary on the home page

Example order:

```text
Customer: Will
Phone: 0411 142 056
Address: Gold Coast
Order: Pulled pork burger and chips
Status: Pending
Driver: Unassigned
```

## What I’m Learning

- Creating a Flask web app
- Using routes
- Using HTML templates
- Using CSS styling
- Creating forms with Flask-WTF
- Reading form data
- Saving data to a database
- Displaying database records on a webpage
- Editing database records
- Deleting database records
- Using Flask-SQLAlchemy
- Using Flask-Migrate
- Creating database models
- Creating database relationships
- Using seed data
- Keeping a project organised
- Making clean Git commits along the way

## Project Pages

The app has these main pages:

```text
/                    Home page
/orders              View all orders
/orders/new          Create a new order
/orders/<id>/edit    Edit an existing order
```

## How the App Works

The app follows a simple flow:

```text
HTML form → Flask route → Python logic → Database → HTML page
```

In simple words:

1. The user fills in an order form
2. The form sends the data to Flask
3. Flask checks the form data
4. Flask saves the order to the database
5. The orders page displays the saved order
6. The user can edit or delete the order later

## Main Files

```text
porkiesdialarib.py              Starts the app
config.py                       Stores database settings
seed.py                         Adds test driver data

app/__init__.py                 Creates the Flask app and database connection
app/routes.py                   Controls the pages and CRUD logic
app/models.py                   Creates the database tables
app/forms.py                    Creates the form fields

app/templates/base.html         Main page layout
app/templates/index.html        Home page
app/templates/orders.html       Orders list page
app/templates/neworder.html     New order form page
app/templates/editorder.html    Edit order form page

app/static/css/style.css        Styling

migrations/                     Database migration files
requirements.txt                Python packages needed for the app
```

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/Porkies_CRUD
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

Before the app can save orders, the database needs to be set up.

Run:

```bash
flask --app porkiesdialarib:app db upgrade
```

This creates the database tables.

Tip: if the orders page or driver dropdown is not working, try running this command again.

## Step 5 — Add Test Drivers 🚗

The app has a driver dropdown. To add example drivers, run:

```bash
python3 seed.py
```

This adds test drivers such as:

```text
Will
Dan
Sarah
```

These drivers can then be selected when creating or editing an order.

## Step 6 — Run the App 🚀

Start the Flask app:

```bash
flask --app porkiesdialarib:app run --debug
```

Open this link in the browser:

```text
http://127.0.0.1:5000
```

The `--debug` part is useful while learning because it helps show errors clearly.

## Step 7 — Create an Order ✅

Open:

```text
http://127.0.0.1:5000/orders/new
```

Try entering:

```text
Customer Name: Will
Customer Phone: 0411 142 056
Customer Address: Gold Coast
Order Details: Pulled pork burger and chips
Status: Pending
Driver: Unassigned
```

Submit the form.

You should be taken to the orders page and see the new order.

## Step 8 — Check the Orders Page 📋

Open:

```text
http://127.0.0.1:5000/orders
```

You should see all saved orders.

From this page, you can:

- View orders
- Edit orders
- Delete orders

This means the main CRUD features are working.

## Step 9 — Edit an Order ✏️

On the orders page, click:

```text
Edit
```

Change something, such as the order status:

```text
Pending → Delivered
```

Save the order.

You should return to the orders page and see the updated information.

## Step 10 — Delete an Order 🗑️

On the orders page, click:

```text
Delete
```

The order should be removed from the table.

This completes the full CRUD cycle.

## Step 11 — Stop the App 🛑

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
flask --app porkiesdialarib:app run --debug
```

### A Package Is Missing

Install the requirements again:

```bash
pip install -r requirements.txt
```

### Database Is Not Working

Run:

```bash
flask --app porkiesdialarib:app db upgrade
```

### No Such Table Error

If you see an error like:

```text
sqlite3.OperationalError: no such table
```

It usually means the database tables have not been created yet.

Run:

```bash
flask --app porkiesdialarib:app db upgrade
```

### Driver Dropdown Only Shows Unassigned

Run the seed file:

```bash
python3 seed.py
```

Then refresh the app.

### The Page Will Not Load

Make sure the app is running:

```bash
flask --app porkiesdialarib:app run --debug
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

Do not upload local database files either.

Avoid uploading:

```text
venv/
__pycache__/
*.db
app.db
.env
.DS_Store
```

Upload the code, templates, migrations, CSS, and `requirements.txt`, not the virtual environment or local database.

## Build Checklist

Use this checklist when recreating the project:

- [ ] Create the project folder
- [ ] Create a virtual environment
- [ ] Install the packages
- [ ] Add the Flask app setup
- [ ] Add the database models
- [ ] Add the order form
- [ ] Add database migrations
- [ ] Add the order list page
- [ ] Add the create order page
- [ ] Add the edit order page
- [ ] Add the delete order feature
- [ ] Add seed data for drivers
- [ ] Add HTML templates
- [ ] Add CSS styling
- [ ] Run the database upgrade
- [ ] Run the seed file
- [ ] Start the app
- [ ] Test creating an order
- [ ] Test viewing orders
- [ ] Test editing an order
- [ ] Test deleting an order

## Suggested Commit Order

This project was built step by step with small commits:

```text
feat: add porkies flask app setup
feat: add database models
feat: add order form
chore: add database migrations
feat: display orders
feat: create new orders
feat: edit existing orders
feat: delete orders
feat: add driver seed script
style: add porkies html layout
docs: add porkies crud readme
```

This makes the project easier to teach because each commit introduces one clear idea.

## Acknowledgement

Special thanks to Dan for allowing me to use and adapt the Porkies project as part of my learning and future teaching.

This project helped me practise Flask, understand CRUD structure, work with databases, and create a beginner-friendly example I can use with students.
