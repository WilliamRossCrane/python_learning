# AdventurePath Web — Choose Your Own Adventure Game 🗺️🌲

A beginner-friendly Flask web game where players choose their own path through an interactive story.

AdventurePath is a creative coding project that teaches students how websites can move between pages, respond to user choices, and create different outcomes.

This project is designed for students learning beginner Flask, HTML, CSS, routes, templates, links, and branching logic.

---

## About the Project

AdventurePath is a **choose-your-own-adventure web game**.

The player begins at the edge of a mysterious forest and chooses where to go.

Each choice sends the player to a different page.

Some choices lead to victory.

Some choices lead to game over.

The project does **not** use a database and does **not** use a REST API.

Instead, it focuses on:

- Flask routes
- HTML templates
- Links between pages
- Branching story paths
- User choice
- Reusable layouts
- CSS styling
- Basic website structure
- Simple game design

---

## What the Game Does

The game lets a player:

- Start an adventure
- Choose between different paths
- Explore a forest
- Explore a cave
- Meet a silver-eyed fox
- Find hidden treasure
- Reach a victory ending
- Reach a game over ending
- Replay the story and try different choices

Example story path:

```text
Home → Start Adventure → Forest → Talk to the Fox → Victory
```

Another story path:

```text
Home → Start Adventure → Cave → Open the Stone Door → Game Over
```

---

## What Students Are Learning

This project teaches two types of skills.

### Coding Skills

Students practise:

- Creating a Flask web app
- Using routes
- Rendering HTML templates
- Using `url_for`
- Linking pages together
- Creating a shared base layout
- Using HTML sections
- Writing CSS styles
- Making buttons and choice cards
- Creating branching paths
- Testing different user journeys

### Thinking Skills

Students practise:

- Planning an interactive story
- Breaking a story into smaller pages
- Thinking about cause and effect
- Designing choices and outcomes
- Testing all possible paths
- Reflecting on how users move through a website

---

## Key Coding Idea — What Is a Route?

A route tells Flask what page to show when someone visits a URL.

Example:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

This means:

```text
When the user visits /
show the index.html page
```

Another example:

```python
@app.route("/forest")
def forest():
    return render_template("forest.html")
```

This means:

```text
When the user visits /forest
show the forest.html page
```

Routes are one of the most important ideas in Flask.

---

## Key Coding Idea — What Is a Template?

A template is an HTML file used by Flask.

Instead of writing all the HTML inside Python, Flask uses templates.

Example:

```python
return render_template("start.html")
```

This tells Flask to show:

```text
app/templates/start.html
```

Templates help keep the project organised.

Python controls the logic.

HTML controls the page structure.

CSS controls the design.

---

## Key Coding Idea — What Is `url_for`?

`url_for` helps Flask create links to routes.

Instead of writing this:

```html
<a href="/forest">Enter the Forest</a>
```

We write this:

```html
<a href="{{ url_for('forest') }}">Enter the Forest</a>
```

This is useful because Flask can find the correct route by the function name.

Example:

```python
@app.route("/forest")
def forest():
    return render_template("forest.html")
```

The function name is:

```text
forest
```

So the HTML link uses:

```html
{{ url_for('forest') }}
```

---

## Key Coding Idea — Branching Logic

AdventurePath uses branching logic.

Branching means the story changes depending on what the player chooses.

Example:

```text
Start
├── Forest
│   ├── Talk to Fox → Victory
│   └── Follow Footprints → Game Over
│
└── Cave
    ├── Light Torch → Treasure → Victory
    └── Open Stone Door → Game Over
```

This is similar to an algorithm because each choice leads to a different next step.

---

## Game Map

The full game path looks like this:

```text
/
└── /start
    ├── /forest
    │   ├── /fox
    │   │   └── /victory
    │   └── /game-over
    │
    └── /cave
        ├── /treasure
        │   └── /victory
        └── /game-over
```

---

## Main Pages

```text
/              Home page
/start         Beginning of the adventure
/forest        Forest path
/cave          Cave path
/fox           Fox story path
/treasure      Treasure story path
/victory       Winning ending
/game-over     Losing ending
```

---

## Main Files

```text
adventurepath.py                 Starts the Flask app
requirements.txt                 Python packages needed for the project
README.md                        Project instructions and explanation

app/__init__.py                  Creates the Flask app
app/routes.py                    Controls the story pages and routes

app/templates/base.html          Main layout shared by all pages
app/templates/index.html         Home page
app/templates/start.html         Start of the adventure
app/templates/forest.html        Forest choice page
app/templates/cave.html          Cave choice page
app/templates/fox.html           Fox path page
app/templates/treasure.html      Treasure path page
app/templates/victory.html       Victory ending page
app/templates/game_over.html     Game over ending page

app/static/css/style.css         Styling for the adventure game
```

---

## How the App Works

The app follows this flow:

```text
Player clicks a link → Flask route runs → HTML template displays → Player chooses next path
```

In simple words:

1. The player opens the website
2. Flask shows the home page
3. The player clicks Start Adventure
4. Flask shows the start page
5. The player chooses Forest or Cave
6. Flask sends them to a new route
7. The player keeps choosing until they reach an ending

---

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/AdventurePath_Web
```

Tip: most commands need to be run from inside the project folder.

---

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

---

## Step 3 — Install the Packages 📦

Install the packages needed for the project:

```bash
pip install -r requirements.txt
```

This installs Flask and any other packages needed to run the app.

---

## Step 4 — Run the App 🚀

Start the Flask app:

```bash
flask --app adventurepath:app run --debug
```

Open this link in your browser:

```text
http://127.0.0.1:5000
```

The `--debug` part is useful while learning because it helps show errors clearly.

---

## Step 5 — Play the Game 🎮

Start at:

```text
http://127.0.0.1:5000
```

Click:

```text
Start Adventure
```

Then try different paths.

Suggested first path:

```text
Start Adventure → Enter the Forest → Talk to the Fox → Victory
```

Suggested second path:

```text
Start Adventure → Explore the Cave → Open the Stone Door → Game Over
```

Try to find all endings.

---

## Step 6 — Stop the App 🛑

To stop the Flask app, go back to the terminal and press:

```text
control + c
```

---

## Test Checklist

Use this checklist to make sure the game works.

- [ ] Home page loads
- [ ] Start Adventure button works
- [ ] Forest path works
- [ ] Cave path works
- [ ] Fox path works
- [ ] Treasure path works
- [ ] Victory page works
- [ ] Game Over page works
- [ ] Play Again links work
- [ ] Back Home links work
- [ ] CSS styling appears correctly

---

## Story Paths to Test

### Forest Victory Path

```text
Home → Start Adventure → Enter the Forest → Talk to the Fox → Victory
```

### Forest Game Over Path

```text
Home → Start Adventure → Enter the Forest → Follow the Glowing Footprints → Game Over
```

### Cave Victory Path

```text
Home → Start Adventure → Explore the Cave → Light the Torch → Treasure → Victory
```

### Cave Game Over Path

```text
Home → Start Adventure → Explore the Cave → Open the Stone Door → Game Over
```

---

## Important HTML Ideas

### Links

Links move the player between pages.

Example:

```html
<a href="{{ url_for('forest') }}">Enter the Forest</a>
```

This creates a clickable link to the forest route.

---

### Sections

Sections help organise content on a page.

Example:

```html
<section class="card">
  <h2>The Journey Begins</h2>
  <p>You wake up at the edge of an ancient forest.</p>
</section>
```

---

### Classes

Classes are used to style HTML with CSS.

Example:

```html
<a class="choice-card" href="{{ url_for('cave') }}">
  <h3>Explore the Cave</h3>
  <p>A dark cave waits nearby.</p>
</a>
```

The class is:

```text
choice-card
```

The CSS file then styles `.choice-card`.

---

## Important CSS Ideas

CSS controls how the website looks.

Example:

```css
.choice-card {
  display: block;
  background: #064e3b;
  border: 1px solid #10b981;
  border-radius: 14px;
  padding: 22px;
  color: #ecfdf5;
  text-decoration: none;
}
```

This changes how each choice looks.

CSS can control:

- Colours
- Font
- Spacing
- Borders
- Buttons
- Hover effects
- Page layout

---

## Common Problems 🛠️

### Flask Command Not Found

Make sure the virtual environment is active:

```bash
source venv/bin/activate
```

Then try running the app again:

```bash
flask --app adventurepath:app run --debug
```

---

### A Package Is Missing

Install the requirements again:

```bash
pip install -r requirements.txt
```

---

### The Page Will Not Load

Make sure the app is running:

```bash
flask --app adventurepath:app run --debug
```

Then open:

```text
http://127.0.0.1:5000
```

---

### Template Not Found

Check that the template file exists inside:

```text
app/templates/
```

Example:

```text
app/templates/index.html
app/templates/start.html
app/templates/forest.html
```

Also check the spelling in `routes.py`.

Example:

```python
return render_template("forest.html")
```

The file must be called:

```text
forest.html
```

---

### Link Not Working

Check that the function name in `url_for` matches the route function name.

Example route:

```python
@app.route("/forest")
def forest():
    return render_template("forest.html")
```

Correct link:

```html
<a href="{{ url_for('forest') }}">Enter the Forest</a>
```

Incorrect link:

```html
<a href="{{ url_for('forest_path') }}">Enter the Forest</a>
```

There is no function called `forest_path`, so Flask will not know where to send the player.

---

### CSS Not Showing

Check that `base.html` links to the CSS file:

```html
<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/style.css') }}"
/>
```

Also check that the CSS file is here:

```text
app/static/css/style.css
```

---

## Important GitHub Note ⚠️

Do not upload the `venv` folder to GitHub.

The `venv` folder belongs to your own computer and can be recreated later.

Other people can recreate it by running:

```bash
python3 -m venv venv
pip install -r requirements.txt
```

Avoid uploading:

```text
venv/
__pycache__/
.env
.DS_Store
```

Upload the code, templates, CSS, README, and `requirements.txt`.

---

## Build Checklist

Use this checklist when recreating the project:

- [ ] Create the project folder
- [ ] Create a virtual environment
- [ ] Install Flask
- [ ] Add the Flask app setup
- [ ] Add the home page
- [ ] Add the start page
- [ ] Add the first story choices
- [ ] Add the forest path
- [ ] Add the cave path
- [ ] Add the ending pages
- [ ] Add the shared base template
- [ ] Add CSS styling
- [ ] Run the app
- [ ] Test all story paths
- [ ] Fix broken links
- [ ] Improve the story
- [ ] Improve the design

---

## Suggested Commit Order

This project was built step by step with small commits:

```text
chore: create adventure path project structure
feat: add flask app setup
feat: add start page
feat: add first story choices
feat: add forest path
feat: add cave path
feat: add ending pages
style: add adventure theme
docs: add adventure path readme
```

This makes the project easier to teach because each commit introduces one clear idea.

---

## Extension Ideas

Students could extend the project by adding:

- More story paths
- More endings
- A score system
- Player health
- Inventory items
- A character name input
- A map page
- Background images
- Sound effects
- A random event route
- A final score or rank
- A mystery ending
- A secret route

---

## Challenge Ideas

### Beginner Challenge

Add one new page to the adventure.

Example:

```text
/river
```

Add a link to it from another page.

---

### Intermediate Challenge

Add a new branch with two choices.

Example:

```text
River
├── Build a raft → Victory
└── Swim across → Game Over
```

---

### Advanced Challenge

Add a simple score using Flask sessions.

Example:

```text
Safe choice = +1
Risky choice = 0
Final page shows score
```

---

## Student Reflection Questions

After completing the project, students could answer:

1. What does a Flask route do?
2. What does `render_template` do?
3. What does `url_for` do?
4. How does the game create different story paths?
5. Which page was easiest to build?
6. Which link or route was hardest to fix?
7. How does CSS change the feel of the game?
8. What new path would you add next?
9. How could you make the game more interactive?
10. How is this project similar to an algorithm?

---

## Why This Project Matters

AdventurePath shows that coding is not only about calculations or data.

Coding can also be creative.

With routes, templates, links, and CSS, students can build interactive stories, games, learning tools, and digital experiences.

Every page is part of a system.

Every link is a choice.

Every choice changes the path.

---

## Acknowledgement

This project was created as a beginner-friendly Flask project for students learning web development, interactive design, and branching logic.

It helps students connect coding with storytelling, creativity, problem-solving, and user experience.
