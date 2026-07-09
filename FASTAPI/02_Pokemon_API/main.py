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


# This model is used when someone updates an existing Pokemon.
# The user sends the new name, type, and level.
# The ID stays the same because it comes from the URL.

class PokemonUpdate(BaseModel):
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
# The Pokemon ID comes from the URL.
# The new Pokemon details come from the JSON body.

@app.put("/pokemon/{pokemon_id}", response_model=Pokemon)
def update_pokemon(pokemon_id: int, updated_pokemon: PokemonUpdate):

    # enumerate() gives us both:
    # - the position in the list
    # - the Pokemon at that position

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