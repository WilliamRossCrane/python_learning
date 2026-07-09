# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Create the FastAPI app.
# Uvicorn looks for this variable when we run:
# uvicorn main:app --reload

app = FastAPI(
    title="Pokemon Learning API",
    description="A beginner FastAPI project for learning REST APIs.",
    version="0.1.0",
)


# A model describes what data should look like.
# This Pokemon model says every Pokemon should have:
# - id: a whole number
# - name: text
# - type: text
# - level: a whole number

class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    level: int


# This list is our temporary Pokemon data.
# Each Pokemon now uses the Pokemon model instead of a plain dictionary.

pokemon: list[Pokemon] = [
    Pokemon(id=1, name="Bulbasaur", type="Grass", level=5),
    Pokemon(id=2, name="Charmander", type="Fire", level=5),
    Pokemon(id=3, name="Squirtle", type="Water", level=5),
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


# response_model tells FastAPI what shape the response should have.
# This route returns a list of Pokemon.

@app.get("/pokemon", response_model=list[Pokemon])
def get_all_pokemon():
    return pokemon


# Test this route:
# curl -X GET "http://127.0.0.1:8000/pokemon"


# This route returns one Pokemon by ID.
# {pokemon_id} is a path parameter.

@app.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def get_pokemon_by_id(pokemon_id: int):

    # Loop through each Pokemon in the list.
    for single_pokemon in pokemon:

        # Because we are using a model, we use dot notation.
        # Example: single_pokemon.id
        if single_pokemon.id == pokemon_id:
            return single_pokemon

    # If no Pokemon was found, return a 404 error.
    raise HTTPException(status_code=404, detail="Pokemon not found")


# Test this route:
# curl -X GET "http://127.0.0.1:8000/pokemon/1"