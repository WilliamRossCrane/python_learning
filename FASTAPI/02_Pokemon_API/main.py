# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

from enum import Enum

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


# Create the FastAPI app.
# Uvicorn looks for this variable when we run:
# uvicorn main:app --reload

app = FastAPI(
    title="Pokemon Learning API",
    description="A beginner FastAPI project for learning REST APIs.",
    version="0.1.0",
)


# An Enum is a list of allowed choices.
# This helps stop users from entering random Pokemon types.
# Example: "Fire" is allowed, but "Banana" is not.

class PokemonType(str, Enum):
    GRASS = "Grass"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    NORMAL = "Normal"
    PSYCHIC = "Psychic"


# A model describes what data should look like.
# This Pokemon model is used when the API returns Pokemon data.

class Pokemon(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=30)
    type: PokemonType
    level: int = Field(..., ge=1, le=100)


# This model is used when someone creates a new Pokemon.
# The user does not need to send an ID.
# The API will create the ID automatically.

class PokemonCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    type: PokemonType
    level: int = Field(..., ge=1, le=100)


# This model is used when someone updates an existing Pokemon.
# The user sends the new name, type, and level.
# The ID stays the same because it comes from the URL.

class PokemonUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    type: PokemonType
    level: int = Field(..., ge=1, le=100)


# This list is our temporary Pokemon data.
# Each Pokemon uses the Pokemon model.

pokemon: list[Pokemon] = [
    Pokemon(id=1, name="Bulbasaur", type=PokemonType.GRASS, level=5),
    Pokemon(id=2, name="Charmander", type=PokemonType.FIRE, level=5),
    Pokemon(id=3, name="Squirtle", type=PokemonType.WATER, level=5),
]


# This helper function finds the position of a Pokemon in the list.
# It returns the index if the Pokemon exists.
# It returns None if the Pokemon does not exist.

def find_pokemon_index_by_id(pokemon_id: int) -> int | None:

    for index, single_pokemon in enumerate(pokemon):

        if single_pokemon.id == pokemon_id:
            return index

    return None


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
# It can also filter Pokemon by type or search by name using query parameters.
#
# Examples:
# /pokemon
# /pokemon?pokemon_type=Fire
# /pokemon?pokemon_name=char
# /pokemon?pokemon_type=Fire&pokemon_name=char

@app.get("/pokemon", response_model=list[Pokemon])
def get_all_pokemon(
    pokemon_type: PokemonType | None = None,
    pokemon_name: str | None = None,
):

    results = pokemon

    if pokemon_type is not None:

        filtered_by_type = []

        for single_pokemon in results:

            if single_pokemon.type == pokemon_type:
                filtered_by_type.append(single_pokemon)

        results = filtered_by_type

    if pokemon_name is not None:

        filtered_by_name = []

        for single_pokemon in results:

            if pokemon_name.lower() in single_pokemon.name.lower():
                filtered_by_name.append(single_pokemon)

        results = filtered_by_name

    return results


# This route returns simple stats about the Pokemon list.
# It calculates:
# - how many Pokemon are in the API
# - how many Pokemon there are for each type

@app.get("/pokemon/stats")
def get_pokemon_stats():

    type_counts = {}

    for single_pokemon in pokemon:

        type_name = single_pokemon.type.value

        if type_name in type_counts:
            type_counts[type_name] += 1
        else:
            type_counts[type_name] = 1

    return {
        "total_pokemon": len(pokemon),
        "type_counts": type_counts,
    }

# This route returns the available Pokemon types.
# It uses the PokemonType enum to build the list.
# This helps users know what type values are allowed.

@app.get("/pokemon/types")
def get_available_pokemon_types():

    available_types = []

    for pokemon_type in PokemonType:
        available_types.append(pokemon_type.value)

    return {
        "available_types": available_types,
    }


# Test this route:
# curl -X GET "http://127.0.0.1:8000/pokemon/types"

# This route returns one Pokemon by ID.

@app.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def get_pokemon_by_id(pokemon_id: int):

    pokemon_index = find_pokemon_index_by_id(pokemon_id)

    if pokemon_index is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return pokemon[pokemon_index]


# This route creates a new Pokemon.
# POST means the user is sending new data to the API.

@app.post("/pokemon", response_model=Pokemon, status_code=status.HTTP_201_CREATED)
def create_pokemon(new_pokemon: PokemonCreate):

    if pokemon:
        new_id = pokemon[-1].id + 1
    else:
        new_id = 1

    pokemon_to_add = Pokemon(
        id=new_id,
        name=new_pokemon.name,
        type=new_pokemon.type,
        level=new_pokemon.level,
    )

    pokemon.append(pokemon_to_add)

    return pokemon_to_add


# This route updates an existing Pokemon.
# PUT means the user is replacing existing data.

@app.put("/pokemon/{pokemon_id}", response_model=Pokemon)
def update_pokemon(pokemon_id: int, updated_pokemon: PokemonUpdate):

    pokemon_index = find_pokemon_index_by_id(pokemon_id)

    if pokemon_index is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    pokemon_to_update = Pokemon(
        id=pokemon_id,
        name=updated_pokemon.name,
        type=updated_pokemon.type,
        level=updated_pokemon.level,
    )

    pokemon[pokemon_index] = pokemon_to_update

    return pokemon_to_update


# This route deletes an existing Pokemon.
# DELETE means the user wants to remove data from the API.

@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):

    pokemon_index = find_pokemon_index_by_id(pokemon_id)

    if pokemon_index is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    deleted_pokemon = pokemon.pop(pokemon_index)

    return {
        "message": f"{deleted_pokemon.name} was deleted.",
        "deleted_pokemon": deleted_pokemon,
    }


# Test valid create:
#
# curl -X POST "http://127.0.0.1:8000/pokemon" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Pikachu", "type": "Electric", "level": 7}'
#
# Test invalid create:
#
# curl -X POST "http://127.0.0.1:8000/pokemon" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Pikachu", "type": "Banana", "level": 7}'