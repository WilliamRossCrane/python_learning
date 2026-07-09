# FastAPI docs:
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc:      http://127.0.0.1:8000/redoc
# OpenAPI:    http://127.0.0.1:8000/openapi.json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Create the FastAPI app.
app = FastAPI()


# This model describes what an item should look like.
# text must be a string.
# is_done is a boolean and starts as False if not provided.
class Item(BaseModel):
    text: str
    is_done: bool = False


# This list stores our items while the server is running.
# This is temporary memory. If the server restarts, the list becomes empty.
items: list[Item] = []


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Add the new item to the list.
    items.append(item)

    # Return the item that was created.
    return item


# Test this POST route in a second terminal:
# curl -X POST "http://127.0.0.1:8000/items" \
#      -H "Content-Type: application/json" \
#      -d '{"text": "apple", "is_done": false}'


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    # Return the first items up to the limit.
    return items[0:limit]


# Test this GET route:
# curl -X GET "http://127.0.0.1:8000/items"


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    # Check that the item exists before trying to return it.
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")

    return items[item_id]


# Test this GET route:
# curl -X GET "http://127.0.0.1:8000/items/0"