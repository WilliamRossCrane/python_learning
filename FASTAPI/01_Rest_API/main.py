from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item

# Test this POST route in the terminal with:
# curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item