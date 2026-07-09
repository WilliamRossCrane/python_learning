# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

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


# A model describes what data should look like.
# This Pokemon model is used when the API returns Pokemon data.

class Pokemon(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=30)
    type: str = Field(..., min_length=3, max_length=20)
    level: int = Field(..., ge=1, le=100)


# This model is used when someone creates a new Pokemon.
# The user does not need to send an ID.
# The API will create the ID automatically.

class PokemonCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    type: str = Field(..., min_length=3, max_length=20)
    level: int = Field(..., ge=1, le=100)


# This model is used when someone updates an existing Pokemon.
# The user sends the new name, type, and level.
# The ID stays the same because it comes from the URL.

class PokemonUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    type: str = Field(..., min_length=3, max_length=20)
    level: int = Field(..., ge=1, le=100)


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
# It can also filter Pokemon by type or search by name using query parameters.
#
# Examples:
# /pokemon
# /pokemon?pokemon_type=Fire
# /pokemon?pokemon_name=char
# /pokemon?pokemon_type=Fire&pokemon_name=char

@app.get("/pokemon", response_model=list[Pokemon])
def get_all_pokemon(
    pokemon_type: str | None = None,
    pokemon_name: str | None = None,
):

    # Start with the full Pokemon list.
    # Then we filter it step by step.

    results = pokemon

    # Filter by type if pokemon_type was provided.

    if pokemon_type is not None:

        filtered_by_type = []

        for single_pokemon in results:

            if single_pokemon.type.lower() == pokemon_type.lower():
                filtered_by_type.append(single_pokemon)

        results = filtered_by_type

    # Search by name if pokemon_name was provided.
    # This uses "in" so partial searches work.
    # Example: "char" will match "Charmander".

    if pokemon_name is not None:

        filtered_by_name = []

        for single_pokemon in results:

            if pokemon_name.lower() in single_pokemon.name.lower():
                filtered_by_name.append(single_pokemon)

        results = filtered_by_name

    return results


# This route returns one Pokemon by ID.

@app.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def get_pokemon_by_id(pokemon_id: int):

    for single_pokemon in pokemon:

        if single_pokemon.id == pokemon_id:
            return single_pokemon

    raise HTTPException(status_code=404, detail="Pokemon not found")


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

    for index, single_pokemon in enumerate(pokemon):

        if single_pokemon.id == pokemon_id:

            pokemon_to_update = Pokemon(
                id=pokemon_id,
                name=updated_pokemon.name,
                type=updated_pokemon.type,
                level=updated_pokemon.level,
            )

            pokemon[index] = pokemon_to_update

            return pokemon_to_update

    raise HTTPException(status_code=404, detail="Pokemon not found")


# This route deletes an existing Pokemon.
# DELETE means the user wants to remove data from the API.
# The Pokemon ID comes from the URL.

@app.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int):

    for index, single_pokemon in enumerate(pokemon):

        if single_pokemon.id == pokemon_id:

            # pop() removes an item from a list.
            # We use the index to remove the correct Pokemon.

            deleted_pokemon = pokemon.pop(index)

            return {
                "message": f"{deleted_pokemon.name} was deleted.",
                "deleted_pokemon": deleted_pokemon,
            }

    raise HTTPException(status_code=404, detail="Pokemon not found")


# Test the create route:
#
# curl -X POST "http://127.0.0.1:8000/pokemon" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Pikachu", "type": "Electric", "level": 7}'
#
# Test the update route:
#
# curl -X PUT "http://127.0.0.1:8000/pokemon/4" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "Raichu", "type": "Electric", "level": 22}'
#
# Test the delete route:
#
# curl -X DELETE "http://127.0.0.1:8000/pokemon/1"