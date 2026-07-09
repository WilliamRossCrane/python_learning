````markdown
# Flask

Flask is a Python framework used to build web apps and APIs.

Flask is useful for:

- websites
- forms
- dashboards
- APIs
- backend projects
- database apps
- CRUD projects

Flask is a good first web framework because it is simple and easy to understand.

---

## What Flask Does

Flask lets Python respond to web requests.

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
```

When the user visits:

```text
http://127.0.0.1:5000
```

Flask runs the `home()` function and returns a response.

---

## Key Ideas

### App

The Flask app is created with:

```python
app = Flask(__name__)
```

This creates the web application.

---

### Route

A route is a URL the app responds to.

```python
@app.route("/")
def home():
    return "Home page"
```

This means when someone visits `/`, Flask runs the `home()` function.

---

### Function

The function decides what happens when the route is visited.

```python
def home():
    return "Welcome to my website"
```

---

### Template

A template is an HTML file Flask can show in the browser.

```python
from flask import render_template

return render_template("index.html")
```

Templates are used when you want proper web pages.

---

### Form

Flask can collect information from forms.

Example uses:

```text
login forms
contact forms
search forms
student input forms
```

---

### JSON

Flask can also return JSON data.

```python
return {"message": "Hello"}
```

This is useful for APIs.

---

## Common Flask Imports

```python
from flask import Flask
```

Creates the Flask app.

```python
from flask import render_template
```

Shows HTML templates.

```python
from flask import request
```

Gets form data or request information.

```python
from flask import jsonify
```

Returns JSON data.

---

## Flask vs FastAPI

Simple version:

```text
Flask = great for learning web apps
FastAPI = great for learning modern APIs
```

Both are useful.

Flask is especially good for learning:

- routes
- templates
- forms
- CRUD
- databases
- simple full-stack apps

---

## Notes

This folder is for learning how Python can build web apps, APIs, forms, dashboards, and backend projects.
````
