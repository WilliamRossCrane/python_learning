# FastAPI

FastAPI is a modern web framework for Python.

It is mainly used to build APIs, backend services, JSON responses, data systems, and modern web app backends.

FastAPI is a good next step after Flask because it teaches more modern backend ideas like:

- APIs
- JSON
- type hints
- request bodies
- validation
- automatic documentation
- backend services

Flask is great for learning how websites work.

FastAPI is great for learning how modern apps talk to each other behind the scenes.

---

## What FastAPI Does

FastAPI lets Python respond to web requests.

For example, when someone visits a route like:

```text
/about
```

FastAPI can run Python code and return data.

FastAPI usually returns data as JSON.

JSON looks like this:

```json
{
  "message": "Hello, FastAPI!"
}
```

This is useful because websites, mobile apps, games, and dashboards often need to send and receive data.

---

## What Is An API?

API stands for:

```text
Application Programming Interface
```

That sounds scary, but the idea is simple.

An API lets different programs talk to each other.

For example:

```text
A weather app asks an API for the forecast.
A game asks an API for player stats.
A website asks an API for products.
A school dashboard asks an API for student data.
A music app asks an API for playlists.
```

The user might see a nice button or screen.

But behind the scenes, apps are often sending requests to APIs.

---

## Why FastAPI is Useful ✨

FastAPI is useful because it is:

- modern
- fast
- clear
- great for APIs
- good for backend projects
- built around Python type hints
- helpful for validation
- able to create automatic API docs
- useful for real-world software development

FastAPI helps you write code that is easier to test, explain, and connect to other apps.

---

## Important FastAPI Ideas

### App

A FastAPI app is created using `FastAPI()`.

```python
from fastapi import FastAPI

app = FastAPI()
```

The `app` is the main object that stores your API routes.

---

### Route

A route is a URL that FastAPI responds to.

```python
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

This means when someone visits `/`, FastAPI runs the `home()` function.

---

### Function

The function decides what happens when someone visits a route.

```python
def home():
    return {"message": "Welcome to my API"}
```

In FastAPI, functions usually return dictionaries.

FastAPI turns those dictionaries into JSON automatically.

---

### JSON

JSON is a common format for sending data between apps.

Python dictionary:

```python
{"name": "Will", "age": 26}
```

JSON response:

```json
{
  "name": "Will",
  "age": 26
}
```

They look very similar.

That makes FastAPI beginner-friendly once you understand dictionaries.

---

### Type Hints

FastAPI uses Python type hints.

A type hint tells Python what kind of data we expect.

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

This tells FastAPI that `student_id` should be an integer.

If someone sends the wrong type of data, FastAPI can help catch the mistake.

---

### Path Parameter

A path parameter is a value inside the URL.

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

Example URL:

```text
/students/5
```

FastAPI takes the `5` from the URL and gives it to the function.

---

### Query Parameter

A query parameter comes after a `?` in the URL.

```python
@app.get("/search")
def search_students(name: str):
    return {"searching_for": name}
```

Example URL:

```text
/search?name=Will
```

Query parameters are useful for searching, filtering, and sorting data.

---

### Request Body

A request body is data sent to the API.

For example, an app might send this:

```json
{
  "name": "Alex",
  "score": 85
}
```

FastAPI can receive this data, check it, and use it inside Python.

---

### Pydantic Model

FastAPI often uses Pydantic models to describe data.

A model is like a clear plan for what data should look like.

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    score: int
```

This says a student should have:

```text
name = text
score = whole number
```

This helps FastAPI check that the data is valid.

---

### Automatic Docs

FastAPI automatically creates interactive API documentation.

When your server is running, you can usually visit:

```text
http://127.0.0.1:8000/docs
```

This page lets you test your API routes in the browser.

This is one of the coolest parts of FastAPI.

You can build an API and test it without needing to build a frontend straight away.

---

## Basic FastAPI App

A simple FastAPI app looks like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {
        "framework": "FastAPI",
        "lesson": "Learning how APIs return JSON data"
    }
```

---

## Common FastAPI Imports

```python
from fastapi import FastAPI
```

Used to create the FastAPI app.

```python
from pydantic import BaseModel
```

Used to create data models for request bodies and validation.

```python
from typing import List
```

Used when working with lists of data.

```python
from fastapi import HTTPException
```

Used to return proper error responses.

Example:

```python
raise HTTPException(status_code=404, detail="Item not found")
```

---

## Installing FastAPI ⚙️

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install FastAPI:

```bash
pip install "fastapi[standard]"
```

This installs FastAPI with common standard tools used for development.

---

## Running FastAPI

If your file is called `main.py`, you can run the app with:

```bash
fastapi dev main.py
```

Then open:

```text
http://127.0.0.1:8000
```

To view the automatic API docs, open:

```text
http://127.0.0.1:8000/docs
```

---

## Running With Uvicorn

You may also see FastAPI apps run with Uvicorn:

```bash
uvicorn main:app --reload
```

This means:

```text
main = the file called main.py
app = the FastAPI app object inside that file
--reload = restart the server when code changes
```

This is useful during development.

---

## Stopping FastAPI

To stop the FastAPI server, press:

```bash
Control + C
```

---

## Flask vs FastAPI

Flask and FastAPI are both Python web frameworks, but they are often used a bit differently.

### Flask

Flask is great for:

```text
web pages
HTML templates
forms
small web apps
simple APIs
learning how websites work
```

### FastAPI

FastAPI is great for:

```text
modern APIs
JSON data
backend services
validation
automatic docs
mobile app backends
frontend/backend projects
```

Simple way to remember it:

```text
Flask helps you learn web apps.
FastAPI helps you learn modern APIs.
```

Both are useful.

They just teach different backend skills.

---

## Real-Life FastAPI Connections

FastAPI skills connect to real software ideas.

### Mobile Apps

A mobile app might ask an API for data:

```text
Get my profile
Get my messages
Get my notifications
Update my settings
```

FastAPI can help build those backend routes.

---

### Games

A game might use an API for:

```text
player stats
leaderboards
inventories
achievements
match history
```

The game screen is the frontend.

The API is the backend that stores and sends data.

---

### School Systems

A school system might use an API for:

```text
student profiles
assessment results
attendance data
class lists
feedback reports
```

FastAPI can be used to practise these kinds of backend ideas.

---

### Dashboards

Dashboards often need data from an API.

For example:

```text
How many tasks are complete?
How many tickets are open?
What are the latest results?
Which items need attention?
```

FastAPI can send that data as JSON.

---

## What This Folder Is For

This folder is for learning FastAPI step by step.

The goal is to practise:

- creating API routes
- returning JSON data
- using path parameters
- using query parameters
- receiving request bodies
- using Pydantic models
- validating data
- handling errors
- building CRUD APIs
- testing API routes
- connecting APIs to databases later

---

## Notes

FastAPI is a strong next step after Flask.

Flask helps you understand websites and backend basics.

FastAPI helps you understand how modern apps, dashboards, games, and services communicate using APIs.

This folder is for practising how Python can be used to build clean, modern backend projects 🚀
