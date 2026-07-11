from fastapi import APIRouter, HTTPException

from app.data.pokemon_data import pokemon_list
from app.schemas import (
    PokemonSummary,
    PokemonTypeDetailResponse,
    PokemonTypeListResponse,
)


router = APIRouter(
    prefix="/api/v2",
    tags=["Types"],
)


# This route returns all Pokemon types currently used in the API.
# It builds the list from the Pokemon data.

@router.get("/types", response_model=PokemonTypeListResponse)
def get_all_types():

    types = []

    for pokemon in pokemon_list:

        for single_type in pokemon.types:

            if single_type not in types:
                types.append(single_type)

    types.sort()

    return {
        "count": len(types),
        "results": types,
    }


# This route returns all Pokemon that match one type.
#
# Examples:
# /api/v2/types/fire
# /api/v2/types/water
# /api/v2/types/grass

@router.get("/types/{type_name}", response_model=PokemonTypeDetailResponse)
def get_type_details(type_name: str):

    matching_pokemon = []
    matched_type_name = None

    for pokemon in pokemon_list:

        for single_type in pokemon.types:

            if single_type.lower() == type_name.lower():

                matched_type_name = single_type

                pokemon_summary = PokemonSummary(
                    dex_number=pokemon.dex_number,
                    name=pokemon.name,
                    slug=pokemon.slug,
                    types=pokemon.types,
                    detail_url=f"/api/v2/pokemon/{pokemon.slug}",
                )

                matching_pokemon.append(pokemon_summary)

    if matched_type_name is None:
        raise HTTPException(status_code=404, detail="Pokemon type not found")

    return {
        "name": matched_type_name,
        "pokemon_count": len(matching_pokemon),
        "pokemon": matching_pokemon,
    }