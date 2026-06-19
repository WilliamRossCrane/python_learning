# CreateDex REST API — Flask + JSON + Database 🐉

A beginner-friendly Flask REST API for managing fictional creatures.

This project teaches how to build an API that can create, read, update, and delete data using JSON instead of HTML pages.

## About

CreateDex is a simple REST API where users can manage fantasy creatures.

Each creature has:

- A name
- An element
- A level
- A rarity

Example creature:

```json
{
  "name": "Flameling",
  "element": "Fire",
  "level": 12,
  "rarity": "Rare"
}
```

This project is useful for learning how apps, websites, and tools can talk to a backend server using JSON data.

## What Is a REST API?

A REST API is a way for programs to communicate over the web.

A normal Flask website usually returns HTML pages.

A REST API usually returns JSON data.

In simple words:

```text
Website route → returns HTML for humans
API route     → returns JSON for apps, tools, or other websites
```

Example HTML page:

```text
http://127.0.0.1:5000/orders
```

Example API endpoint:

```text
http://127.0.0.1:5000/api/creatures
```

The API does not show a styled webpage. It sends back structured data.

## What Is JSON?

JSON stands for JavaScript Object Notation.

It looks a lot like a Python dictionary.

Example JSON:

```json
{
  "name": "Aquabub",
  "element": "Water",
  "level": 8,
  "rarity": "Common"
}
```

APIs often use JSON because it is easy for different programming languages and apps to read.

## What the App Does

The app lets a user:

- View all creatures
- View one creature by ID
- Create a new creature
- Update an existing creature
- Delete a creature
- Seed the database with starter creatures

This project demonstrates the full CRUD cycle.

CRUD stands for:

```text
Create
Read
Update
Delete
```

## REST API Methods

REST APIs use HTTP methods to describe the action being performed.

| Method | Meaning     | Example                     |
| ------ | ----------- | --------------------------- |
| GET    | Read data   | Get all creatures           |
| POST   | Create data | Add a new creature          |
| PUT    | Update data | Change an existing creature |
| DELETE | Delete data | Remove a creature           |

## API Endpoints

| Method | Endpoint              | What it does                 |
| ------ | --------------------- | ---------------------------- |
| GET    | `/`                   | API welcome message          |
| GET    | `/api/health`         | Checks if the API is running |
| GET    | `/api/creatures`      | Gets all creatures           |
| GET    | `/api/creatures/<id>` | Gets one creature            |
| POST   | `/api/creatures`      | Creates a new creature       |
| PUT    | `/api/creatures/<id>` | Updates a creature           |
| DELETE | `/api/creatures/<id>` | Deletes a creature           |

## What I’m Learning

- Creating a Flask REST API
- Returning JSON with `jsonify`
- Using API routes
- Using GET, POST, PUT, and DELETE requests
- Reading JSON data from a request
- Saving data to a database
- Updating database records
- Deleting database records
- Using Flask-SQLAlchemy
- Using Flask-Migrate
- Testing APIs with `curl`
- Understanding HTTP status codes
- Keeping a project organised
- Making clean Git commits

## Main Files

```text
createdex.py              Starts the app
config.py                 Stores database settings
seed.py                   Adds starter creature data

app/__init__.py           Creates the Flask app and database connection
app/routes.py             Controls the API endpoints
app/models.py             Creates the Creature database table

migrations/               Database migration files
requirements.txt          Python packages needed for the app
```

## How the App Works

The app follows this flow:

```text
curl/browser request → Flask route → Python logic → Database → JSON response
```

In simple words:

1. A user sends a request to an API endpoint
2. Flask receives the request
3. Flask runs the correct route
4. Flask reads or changes the database
5. Flask returns JSON data

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/createdex_REST
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

Before the API can save creatures, the database needs to be set up.

Run:

```bash
flask --app createdex:app db upgrade
```

This creates the database table.

## Step 5 — Add Starter Creatures 🌱

Run the seed file:

```bash
python3 seed.py
```

This adds starter creatures such as:

```text
Flameling
Aquabub
Thornox
Voltwing
```

Seed data makes it easier to test the API without creating everything manually.

## Step 6 — Run the API 🚀

Start the Flask app:

```bash
flask --app createdex:app run --debug
```

Open this link in the browser:

```text
http://127.0.0.1:5000
```

You should see a JSON welcome message.

The `--debug` part is useful while learning because it helps show errors clearly.

## Step 7 — Test the Health Check ✅

Open this in the browser:

```text
http://127.0.0.1:5000/api/health
```

You should see something like:

```json
{
  "message": "CreateDex API is running.",
  "status": "ok"
}
```

This means the API is running.

## What Is curl?

`curl` is a terminal tool used to send requests to websites and APIs.

A browser is good for testing simple GET requests.

But for POST, PUT, and DELETE requests, `curl` is useful because it lets us choose:

- The HTTP method
- The URL
- The JSON data
- The request headers

Basic curl structure:

```bash
curl -X METHOD URL
```

Example:

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

## Testing the API with curl

Important: keep the Flask app running in one terminal.

Then open a second terminal tab to run the `curl` commands.

## GET — View All Creatures

This gets every creature in the database.

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

You should see something like:

```json
{
  "count": 4,
  "creatures": [
    {
      "id": 1,
      "name": "Flameling",
      "element": "Fire",
      "level": 12,
      "rarity": "Rare"
    }
  ]
}
```

## GET — View One Creature

This gets one creature by its ID.

```bash
curl -X GET http://127.0.0.1:5000/api/creatures/1
```

Example response:

```json
{
  "creature": {
    "id": 1,
    "name": "Flameling",
    "element": "Fire",
    "level": 12,
    "rarity": "Rare"
  }
}
```

If the ID does not exist, Flask will return a 404 error.

## POST — Create a New Creature

This creates a new creature.

```bash
curl -X POST http://127.0.0.1:5000/api/creatures \
-H "Content-Type: application/json" \
-d '{
  "name": "Shadowpup",
  "element": "Dark",
  "level": 10,
  "rarity": "Rare"
}'
```

What this means:

```text
-X POST                              Use the POST method
-H "Content-Type: application/json"  Tell Flask we are sending JSON
-d '{ ... }'                         The JSON data being sent
```

Example response:

```json
{
  "message": "Creature created successfully.",
  "creature": {
    "id": 5,
    "name": "Shadowpup",
    "element": "Dark",
    "level": 10,
    "rarity": "Rare"
  }
}
```

After creating it, check the list again:

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

## PUT — Update a Creature

This updates an existing creature.

Example: update creature ID `1`.

```bash
curl -X PUT http://127.0.0.1:5000/api/creatures/1 \
-H "Content-Type: application/json" \
-d '{
  "name": "Flameling",
  "element": "Fire",
  "level": 20,
  "rarity": "Epic"
}'
```

Example response:

```json
{
  "message": "Creature updated successfully.",
  "creature": {
    "id": 1,
    "name": "Flameling",
    "element": "Fire",
    "level": 20,
    "rarity": "Epic"
  }
}
```

You can also update only one field because this app uses `.get()` in the update route.

Example:

```bash
curl -X PUT http://127.0.0.1:5000/api/creatures/1 \
-H "Content-Type: application/json" \
-d '{
  "level": 25
}'
```

This changes the level but keeps the other values the same.

## DELETE — Delete a Creature

This deletes a creature by ID.

```bash
curl -X DELETE http://127.0.0.1:5000/api/creatures/1
```

Example response:

```json
{
  "message": "Creature deleted successfully."
}
```

Check the list again:

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

The deleted creature should no longer appear.

## Common HTTP Status Codes

APIs use status codes to explain what happened.

| Status Code | Meaning                                            |
| ----------- | -------------------------------------------------- |
| 200         | OK — the request worked                            |
| 201         | Created — new data was created                     |
| 400         | Bad Request — something was wrong with the request |
| 404         | Not Found — the item could not be found            |
| 500         | Server Error — something went wrong in the app     |

Example:

When a creature is created successfully, the API returns:

```text
201 Created
```

When JSON data is missing, the API returns:

```text
400 Bad Request
```

## Full API Testing Flow

Use this order to test the project.

### 1. Start the app

```bash
flask --app createdex:app run --debug
```

### 2. Check the API is running

```bash
curl -X GET http://127.0.0.1:5000/api/health
```

### 3. View all creatures

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

### 4. Create a creature

```bash
curl -X POST http://127.0.0.1:5000/api/creatures \
-H "Content-Type: application/json" \
-d '{
  "name": "Leaflet",
  "element": "Grass",
  "level": 6,
  "rarity": "Common"
}'
```

### 5. View one creature

```bash
curl -X GET http://127.0.0.1:5000/api/creatures/1
```

### 6. Update a creature

```bash
curl -X PUT http://127.0.0.1:5000/api/creatures/1 \
-H "Content-Type: application/json" \
-d '{
  "level": 30,
  "rarity": "Legendary"
}'
```

### 7. Delete a creature

```bash
curl -X DELETE http://127.0.0.1:5000/api/creatures/1
```

## Common Problems 🛠️

### Flask Command Not Found

Make sure the virtual environment is active:

```bash
source venv/bin/activate
```

Then try again:

```bash
flask --app createdex:app run --debug
```

### A Package Is Missing

Install the requirements again:

```bash
pip install -r requirements.txt
```

### Database Is Not Working

Run:

```bash
flask --app createdex:app db upgrade
```

### No Such Table Error

If you see an error like:

```text
sqlite3.OperationalError: no such table
```

It usually means the database table has not been created yet.

Run:

```bash
flask --app createdex:app db upgrade
```

### No Creatures Are Showing

Run the seed file:

```bash
python3 seed.py
```

Then test again:

```bash
curl -X GET http://127.0.0.1:5000/api/creatures
```

### curl Command Not Working

Make sure the Flask app is running in another terminal.

Also check that the URL is correct:

```text
http://127.0.0.1:5000
```

### JSON Error

Make sure your JSON uses double quotes, not single quotes inside the JSON object.

Correct:

```json
{
  "name": "Flameling"
}
```

Incorrect:

```json
{
  "name": "Flameling"
}
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

Upload the code, migrations, seed file, and `requirements.txt`, not the virtual environment or local database.

## Build Checklist

Use this checklist when recreating the project:

- [ ] Create the project folder
- [ ] Create a virtual environment
- [ ] Install the packages
- [ ] Add the Flask API setup
- [ ] Add the Creature model
- [ ] Add database migrations
- [ ] Add the GET all creatures endpoint
- [ ] Add the POST create creature endpoint
- [ ] Add the GET one creature endpoint
- [ ] Add the PUT update creature endpoint
- [ ] Add the DELETE creature endpoint
- [ ] Add seed data
- [ ] Run the database upgrade
- [ ] Run the seed file
- [ ] Start the API
- [ ] Test GET requests
- [ ] Test POST requests
- [ ] Test PUT requests
- [ ] Test DELETE requests

## Suggested Commit Order

This project was built step by step with small commits:

```text
chore: create createdex rest project structure
feat: add flask api setup
feat: add creature model
chore: add creature database migrations
feat: list creatures endpoint
feat: create creature endpoint
feat: get single creature endpoint
feat: update creature endpoint
feat: delete creature endpoint
feat: add creature seed data
docs: add createdex rest readme
```

This makes the project easier to teach because each commit introduces one clear idea.

## Acknowledgement

This project was created as a beginner-friendly REST API example for students learning Flask, databases, JSON, and API testing.

It follows a similar structure to the other Flask learning projects, but focuses on APIs instead of HTML pages.
