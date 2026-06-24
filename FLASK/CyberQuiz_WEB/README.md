# CyberQuest — Phishing Game 🛡️💻

An interactive Flask web game that teaches students how to spot cyber risks and make safer online choices.

CyberQuest is a decision-based cyber safety game. Players read real-world style scenarios, choose what they would do, earn points, and receive a final cyber safety report.

This project is designed for students learning beginner web development, Python, Flask, HTML, CSS, decision logic, and basic cyber safety.

---

## About the Project

CyberQuest is not a database app and it is not a REST API.

Instead, it focuses on:

- Flask routes
- HTML templates
- User choices
- Branching logic
- Sessions
- Scoring
- Cyber safety feedback
- Simple game design

The player is shown cyber safety scenarios about things like phishing emails, MFA codes, passwords, app permissions, and public Wi-Fi.

Each choice gives a different score and feedback.

At the end, the app gives the player a cyber safety rating.

---

## What the Game Teaches

CyberQuest teaches two types of skills.

### Coding Skills

Students practise:

- Creating a Flask web app
- Using routes
- Using HTML templates
- Using Jinja loops
- Sending users between pages
- Handling button clicks
- Using `POST` requests
- Using sessions to store score
- Using lists and dictionaries
- Using if/else statements
- Displaying feedback
- Styling pages with CSS

### Cyber Safety Skills

Students learn about:

- Phishing messages
- Suspicious links
- Multi-Factor Authentication, also called MFA
- Password and passphrase safety
- Digital footprints
- App permissions
- Public Wi-Fi risks
- Slowing down before clicking
- Asking for help when something seems suspicious

---

## What Is Phishing?

Phishing is when someone tries to trick you into giving away information, clicking a dangerous link, or logging into a fake website.

A phishing message might pretend to be from:

- A school
- A bank
- A gaming company
- A delivery company
- A social media app
- A teacher or IT support person

Phishing messages often use pressure or urgency.

Example:

```text
Your account will be deleted today.
Click this link now to keep your account.
```

A safer response would be:

```text
Stop.
Check the sender.
Do not click the link.
Ask a teacher, parent, carer, or IT support person.
```

---

## What Is MFA?

MFA stands for Multi-Factor Authentication.

It means using more than just a password to log in.

Examples include:

- A code sent to your phone
- An authenticator app
- A fingerprint
- A face scan
- A security key

MFA helps protect accounts, but only if you keep the code private.

Important rule:

```text
Never share your MFA code with anyone.
```

Even if someone says they are from tech support, you should not give them your code.

---

## What Is a Digital Footprint?

A digital footprint is the trail of information you leave behind when you use digital systems.

This can include:

- Apps you use
- Websites you visit
- Accounts you create
- Photos you upload
- Comments you post
- Location data
- App permissions
- Search history

CyberQuest helps students think about how everyday choices can add to their digital footprint.

---

## Game Flow

The app follows this basic flow:

```text
Home page → Start game → Scenario → Choice → Score → Next scenario → Final report
```

In simple words:

1. The player starts the game
2. Flask resets their score
3. The player sees a cyber safety scenario
4. The player chooses an answer
5. Flask checks the choice
6. Flask saves the score and feedback
7. The next scenario loads
8. The final report shows the result

---

## Main Pages

```text
/                    Home page
/start               Starts the game
/scenario/<id>       Shows a scenario
/result              Shows the final cyber safety report
```

Example:

```text
http://127.0.0.1:5000/scenario/1
```

This shows scenario number 1.

---

## Main Files

```text
cyberquest.py                  Starts the Flask app
requirements.txt               Python packages needed for the project
README.md                      Project instructions and explanation

app/__init__.py                Creates the Flask app
app/routes.py                  Controls the game pages and scoring logic
app/scenarios.py               Stores the cyber safety scenarios

app/templates/base.html        Main layout shared by all pages
app/templates/index.html       Home page
app/templates/scenario.html    Scenario page
app/templates/result.html      Final report page

app/static/css/style.css       Styling for the game
```

---

## Important Coding Ideas

### 1. Routes

A route tells Flask what to do when someone visits a URL.

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

---

### 2. Templates

Templates are HTML files that Flask can fill with Python data.

Example:

```python
return render_template("scenario.html", scenario=scenario)
```

This sends the `scenario` data into the `scenario.html` page.

---

### 3. Jinja

Jinja lets HTML templates use Python-style logic.

Example:

```html
{{ scenario.title }}
```

This displays the title of the current scenario.

Example loop:

```html
{% for choice in scenario.choices %}
<button>{{ choice.text }}</button>
{% endfor %}
```

This creates one button for each choice.

---

### 4. Scenario Data

The scenarios are stored in:

```text
app/scenarios.py
```

Each scenario is a Python dictionary.

Example:

```python
{
    "id": 1,
    "title": "Suspicious School Email",
    "topic": "Phishing",
    "situation": "You receive an email saying your school account will be deleted unless you click a link.",
    "choices": [
        {
            "text": "Click the link.",
            "score": 0,
            "feedback": "Risky choice. This could be a phishing link.",
        }
    ],
}
```

This is useful because the game content is separate from the route logic.

---

### 5. Forms and POST Requests

The scenario page uses buttons inside a form.

When the player clicks a button, the form sends data back to Flask.

```html
<form method="POST">
  <button type="submit" name="choice_index" value="0">Click the link</button>
</form>
```

The route can then read the selected choice:

```python
choice_index = int(request.form["choice_index"])
```

---

### 6. Sessions

A session lets Flask remember information while the player moves between pages.

CyberQuest uses sessions to remember:

- The player’s score
- The player’s answers
- The feedback for each choice

Example:

```python
session["score"] = 0
```

Then later:

```python
session["score"] = session.get("score", 0) + selected_choice["score"]
```

This means:

```text
Get the current score.
Add the points from the selected choice.
Save the new score.
```

---

### 7. If/Else Logic

The final report uses if/else logic to decide the player’s rating.

Example:

```python
if score >= 8:
    rating = "Cyber Guardian"
elif score >= 5:
    rating = "Cyber Apprentice"
else:
    rating = "Needs More Training"
```

This is branching logic.

The program makes a decision based on the player’s score.

---

## Step 1 — Go Into the Project Folder 📁

Open the terminal and go into the project folder:

```bash
cd FLASK/CyberQuest_PhishingGame
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
flask --app cyberquest:app run --debug
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
Start Game
```

Then read each scenario and choose the safest response.

At the end, you will receive a cyber safety report.

---

## Step 6 — Stop the App 🛑

To stop the Flask app, go back to the terminal and press:

```text
control + c
```

---

## Example Scenario

A scenario might look like this:

```text
You receive an email saying your school account will be deleted unless you click a link and log in immediately.
```

Possible choices:

```text
1. Click the link and log in quickly.
2. Check the sender address and report the email.
3. Forward the email to your friends.
```

The safest answer is usually the one that slows down, checks the source, and asks for help.

---

## Cyber Safety Tips

### Slow Down Before Clicking

Cyber attacks often try to make people rush.

Watch for messages that say:

```text
Act now
Urgent
Final warning
Your account will be deleted
You have won a prize
```

A good rule is:

```text
If it feels rushed, slow down.
```

---

### Check the Sender

Before trusting a message, check:

- Who sent it?
- Does the email address look right?
- Are there spelling mistakes?
- Is the message asking for private information?
- Is there a suspicious link?

---

### Protect Your Passwords

Safer password habits include:

- Use different passwords for different accounts
- Use long passphrases
- Do not use your name or birthday
- Do not share passwords
- Use MFA when available

Example passphrase style:

```text
PurpleTigerSkatesAt7
```

That is usually stronger than something short like:

```text
password123
```

---

### Never Share MFA Codes

An MFA code is like a temporary key to your account.

If someone asks for it, that is suspicious.

Even if they say they are from tech support, do not share it.

---

### Think About App Permissions

If a wallpaper app asks for your camera, microphone, contacts, and location, that is worth questioning.

Ask:

```text
Does this app really need this permission?
```

If not, deny the permission.

---

### Be Careful on Public Wi-Fi

Public Wi-Fi can be useful, but it may not always be safe for important accounts.

Be careful logging into:

- Banking
- School accounts
- Email accounts
- Shopping accounts
- Social media accounts

---

## Common Problems 🛠️

### Flask Command Not Found

Make sure the virtual environment is active:

```bash
source venv/bin/activate
```

Then try running the app again:

```bash
flask --app cyberquest:app run --debug
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
flask --app cyberquest:app run --debug
```

Then open:

```text
http://127.0.0.1:5000
```

---

### The Score Is Not Saving

Check that the app has a secret key in:

```text
app/__init__.py
```

It should include something like:

```python
app.config["SECRET_KEY"] = "cyberquest-secret-key"
```

Flask sessions need a secret key to work.

---

### The Buttons Do Nothing

Check that the scenario route allows both `GET` and `POST`.

It should look like this:

```python
@app.route("/scenario/<int:scenario_id>", methods=["GET", "POST"])
```

If `POST` is missing, Flask will not handle the button click properly.

---

### Template Not Found

Check that your templates are inside:

```text
app/templates/
```

For example:

```text
app/templates/index.html
app/templates/scenario.html
app/templates/result.html
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
- [ ] Add the scenario data
- [ ] Add the home page
- [ ] Add the scenario page
- [ ] Add choice buttons
- [ ] Add POST request handling
- [ ] Add scoring with sessions
- [ ] Add the final report page
- [ ] Add cyber safety advice
- [ ] Add CSS styling
- [ ] Run the app
- [ ] Play through the game
- [ ] Test that the score works
- [ ] Test that the final report appears

---

## Suggested Commit Order

This project was built step by step with small commits:

```text
chore: create cyberquest project structure
feat: add flask app setup
feat: add scenario data
feat: display scenario page
feat: add choice handling and scoring
feat: add final cyber safety report
style: add cyberquest layout
docs: add cyberquest readme
```

This makes the project easier to teach because each commit introduces one clear idea.

---

## Extension Ideas

Students could extend the project by adding:

- More cyber safety scenarios
- A timer for each scenario
- Different difficulty levels
- A progress bar
- More detailed feedback
- A class leaderboard
- A printable cyber safety certificate
- Extra topics like scams, social media privacy, or AI-generated fake images

---

## Student Reflection Questions

After completing the project, students could answer:

1. What was the safest choice in each scenario?
2. Which scenario was hardest to answer?
3. What is one cyber safety habit you could improve?
4. How did the app remember your score?
5. What does a Flask route do?
6. What does a session do?
7. How did the HTML page display different choices?
8. How could this game be improved for younger students?

---

## Acknowledgement

This project was created as a beginner-friendly Flask project for students learning web development, decision logic, and cyber safety.

It connects coding with real online choices students may experience, such as suspicious messages, password safety, MFA codes, app permissions, and public Wi-Fi.
