from fastapi import FastAPI, HTTPException

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
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")