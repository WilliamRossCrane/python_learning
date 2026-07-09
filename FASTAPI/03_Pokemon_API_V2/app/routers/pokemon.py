from fastapi import APIRouter, HTTPException, Query

from app.data.pokemon_data import pokemon_list
from app.schemas import Pokemon, PokemonListResponse, PokemonSummary


router = APIRouter(
    prefix="/api/v2",
    tags=["Pokemon"],
)


# This route returns a paginated list of Pokemon summaries.
# limit controls how many results are returned.
# offset controls where the list starts.

@router.get("/pokemon", response_model=PokemonListResponse)
def get_all_pokemon(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):

    paginated_pokemon = pokemon_list[offset: offset + limit]

    results = []

    for pokemon in paginated_pokemon:

        pokemon_summary = PokemonSummary(
            dex_number=pokemon.dex_number,
            name=pokemon.name,
            slug=pokemon.slug,
            types=pokemon.types,
            detail_url=f"/api/v2/pokemon/{pokemon.slug}",
        )

        results.append(pokemon_summary)

    return {
        "count": len(pokemon_list),
        "limit": limit,
        "offset": offset,
        "results": results,
    }


# This route returns the full data for one Pokemon.
# The user can search by dex number or slug.
#
# Examples:
# /api/v2/pokemon/1
# /api/v2/pokemon/bulbasaur

@router.get("/pokemon/{pokemon_identifier}", response_model=Pokemon)
def get_pokemon(pokemon_identifier: str):

    for pokemon in pokemon_list:

        if str(pokemon.dex_number) == pokemon_identifier:
            return pokemon

        if pokemon.slug.lower() == pokemon_identifier.lower():
            return pokemon

    raise HTTPException(status_code=404, detail="Pokemon not found")