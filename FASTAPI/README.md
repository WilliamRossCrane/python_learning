````markdown
# FastAPI

FastAPI is a Python framework used to build APIs.

An API lets apps send and receive data.

FastAPI is useful for:

- backend projects
- JSON data
- REST APIs
- mobile app backends
- dashboards
- frontend/backend apps

FastAPI is a good next step after Flask because it focuses more on APIs and data.

---

## What FastAPI Does

FastAPI lets Python respond to web requests.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}
```
````

When the user visits:

```text
http://127.0.0.1:8000
```

FastAPI returns:

```json
{
  "message": "Hello, FastAPI!"
}
```

---

## Key Ideas

### Route

A route is a URL the API responds to.

```python
@app.get("/")
def root():
    return {"message": "Home page"}
```

---

### JSON

FastAPI usually returns JSON data.

```python
return {"name": "Alex", "score": 90}
```

---

### Path Parameter

A path parameter gets information from the URL.

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Example:

```text
/items/1
```

---

### Request Body

A request body sends data to the API.

```python
from pydantic import BaseModel

class Item(BaseModel):
    text: str
    is_done: bool = False
```

This helps FastAPI check that the data is correct.

---

## FastAPI Docs

FastAPI creates docs automatically.

When the server is running, open:

```text
http://127.0.0.1:8000/docs
```

This lets you test your API in the browser.

---

## Notes

This folder is for learning how to build simple REST APIs with Python.

```

```
