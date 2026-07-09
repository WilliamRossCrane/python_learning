from fastapi import APIRouter, HTTPException

from app.data.pokemon_data import pokemon_list
from app.schemas import Pokemon


router = APIRouter(
    prefix="/api/v2/pokemon",
    tags=["Pokemon"],
)


@router.get("/", response_model=list[Pokemon])
def get_all_pokemon():
    return pokemon_list


@router.get("/{pokemon_identifier}", response_model=Pokemon)
def get_pokemon(pokemon_identifier: str):

    for pokemon in pokemon_list:

        if str(pokemon.dex_number) == pokemon_identifier:
            return pokemon

        if pokemon.slug.lower() == pokemon_identifier.lower():
            return pokemon

    raise HTTPException(status_code=404, detail="Pokemon not found")