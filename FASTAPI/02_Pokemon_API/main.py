# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

from fastapi import FastAPI


# Create the FastAPI app.
# Uvicorn looks for this variable when we run:
# uvicorn main:app --reload

app = FastAPI(
    title="Pokemon Learning API",
    description="A beginner FastAPI project for learning REST APIs.",
    version="0.1.0",
)


# This list is our temporary Pokemon data.
# Each Pokemon is stored as a dictionary.
# A dictionary stores information using labels called keys.

pokemon = [
    {
        "id": 1,
        "name": "Bulbasaur",
        "type": "Grass",
        "level": 5,
    },
    {
        "id": 2,
        "name": "Charmander",
        "type": "Fire",
        "level": 5,
    },
    {
        "id": 3,
        "name": "Squirtle",
        "type": "Water",
        "level": 5,
    },
]


@app.get("/")
def root():
    return {
        "message": "Welcome to the Pokemon Learning API!",
        "docs": "Go to /docs to test the API.",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "The Pokemon API is running.",
    }


# This route returns all Pokemon.
# GET means the user is asking to read data.
# FastAPI automatically turns the Python list into JSON.

@app.get("/pokemon")
def get_all_pokemon():
    return pokemon


# Test this route in the browser:
# http://127.0.0.1:8000/pokemon
#
# Or test it in the terminal:
# curl -X GET "http://127.0.0.1:8000/pokemon"