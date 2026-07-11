from fastapi import APIRouter, HTTPException

from app.data.pokemon_data import pokemon_list
from app.schemas import (
    AbilityDetailResponse,
    AbilityListResponse,
    PokemonSummary,
)


router = APIRouter(
    prefix="/api/v2",
    tags=["Abilities"],
)


# This helper function turns text into a simple URL-friendly format.
# Example:
# "Solar Power" becomes "solar-power"

def create_slug(text: str) -> str:
    return text.lower().replace(" ", "-")


# This route returns all abilities currently used in the API.
# It builds the list from the Pokemon data.

@router.get("/abilities", response_model=AbilityListResponse)
def get_all_abilities():

    abilities = []

    for pokemon in pokemon_list:

        for ability in pokemon.abilities:

            if ability not in abilities:
                abilities.append(ability)

    abilities.sort()

    return {
        "count": len(abilities),
        "results": abilities,
    }


# This route returns all Pokemon with one ability.
#
# Examples:
# /api/v2/abilities/overgrow
# /api/v2/abilities/blaze
# /api/v2/abilities/solar-power

@router.get("/abilities/{ability_name}", response_model=AbilityDetailResponse)
def get_ability_details(ability_name: str):

    matching_pokemon = []
    matched_ability_name = None

    for pokemon in pokemon_list:

        for ability in pokemon.abilities:

            if create_slug(ability) == create_slug(ability_name):

                matched_ability_name = ability

                pokemon_summary = PokemonSummary(
                    dex_number=pokemon.dex_number,
                    name=pokemon.name,
                    slug=pokemon.slug,
                    types=pokemon.types,
                    detail_url=f"/api/v2/pokemon/{pokemon.slug}",
                )

                matching_pokemon.append(pokemon_summary)

    if matched_ability_name is None:
        raise HTTPException(status_code=404, detail="Pokemon ability not found")

    return {
        "name": matched_ability_name,
        "pokemon_count": len(matching_pokemon),
        "pokemon": matching_pokemon,
    }