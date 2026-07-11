from fastapi import APIRouter, HTTPException

from app.data.pokemon_data import pokemon_list
from app.schemas import (
    GenerationDetailResponse,
    GenerationListResponse,
    PokemonSummary,
)


router = APIRouter(
    prefix="/api/v2",
    tags=["Generations"],
)


# This route returns every generation that appears in the data.
@router.get("/generations", response_model=GenerationListResponse)
def get_all_generations():
    generations = []

    for pokemon in pokemon_list:
        if pokemon.generation not in generations:
            generations.append(pokemon.generation)

    generations.sort()

    return {
        "count": len(generations),
        "results": generations,
    }


# This route returns all Pokemon from one generation.
@router.get("/generations/{generation_number}", response_model=GenerationDetailResponse)
def get_generation_details(generation_number: int):
    matching_pokemon = []

    for pokemon in pokemon_list:
        if pokemon.generation == generation_number:
            pokemon_summary = PokemonSummary(
                dex_number=pokemon.dex_number,
                name=pokemon.name,
                slug=pokemon.slug,
                types=pokemon.types,
                detail_url=f"/api/v2/pokemon/{pokemon.slug}",
            )

            matching_pokemon.append(pokemon_summary)

    if len(matching_pokemon) == 0:
        raise HTTPException(status_code=404, detail="Pokemon generation not found")

    return {
        "generation": generation_number,
        "pokemon_count": len(matching_pokemon),
        "pokemon": matching_pokemon,
    }