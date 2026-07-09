# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

from fastapi import FastAPI, HTTPException, status
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
# This Pokemon model is used when the API returns Pokemon data.

class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    level: int


# This model is used when someone creates a new Pokemon.
# The user does not need to send an ID.
# The API will create the ID automatically.

class PokemonCreate(BaseModel):
    name: str
    type: str
    level: int


# This list is our temporary Pokemon data.
# Each Pokemon uses the Pokemon model.

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


# This route returns all Pokemon.

@app.get("/pokemon", response_model=list[Pokemon])
def get_all_pokemon():
    return pokemon


# This route returns one Pokemon by ID.

@app.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def get_pokemon_by_id(pokemon_id: int):

    for single_pokemon in pokemon:

        if single_pokemon.id == pokemon_id:
            return single_pokemon

    raise HTTPException(status_code=404, detail="Pokemon not found")


# This route creates a new Pokemon.
# POST means the user is sending data to the API.
# status_code=201 means something new was created.

@app.post("/pokemon", response_model=Pokemon, status_code=status.HTTP_201_CREATED)
def create_pokemon(new_pokemon: PokemonCreate):

    # Create a new ID.
    # If the list has Pokemon, add 1 to the last Pokemon ID.
    # If the list is empty, start at 1.

    if pokemon:
        new_id = pokemon[-1].id + 1
    else:
        new_id = 1

    # Create the new Pokemon using the Pokemon model.

    pokemon_to_add = Pokemon(
        id=new_id,
        name=new_pokemon.name,
        type=new_pokemon.type,
        level=new_pokemon.level,
    )

    # Add the new Pokemon to the list.

    pokemon.append(pokemon_to_add)

    # Return the new Pokemon.

    return pokemon_to_add


# Test this POST route:
#
# curl -X POST "http://127.0.0.1:8000/pokemon" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Pikachu", "type": "Electric", "level": 7}'