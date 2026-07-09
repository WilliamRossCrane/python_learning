from fastapi import APIRouter, HTTPException, Query

from app.data.pokemon_data import pokemon_list
from app.schemas import Pokemon, PokemonListResponse, PokemonSummary


router = APIRouter(
    prefix="/api/v2",
    tags=["Pokemon"],
)


# This route returns a paginated list of Pokemon summaries.
# It can also search and filter Pokemon using query parameters.
#
# Examples:
# /api/v2/pokemon
# /api/v2/pokemon?name=char
# /api/v2/pokemon?type=Fire
# /api/v2/pokemon?region=Kanto
# /api/v2/pokemon?generation=1
# /api/v2/pokemon?type=Fire&region=Kanto

@router.get("/pokemon", response_model=PokemonListResponse)
def get_all_pokemon(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    name: str | None = None,
    pokemon_type: str | None = Query(default=None, alias="type"),
    region: str | None = None,
    generation: int | None = None,
    is_legendary: bool | None = None,
):

    # Start with the full Pokemon list.
    # Then filter it step by step.

    filtered_pokemon = pokemon_list

    # Search by name.
    # This is a partial search, so "char" matches "Charmander".

    if name is not None:

        name_results = []

        for pokemon in filtered_pokemon:

            if name.lower() in pokemon.name.lower():
                name_results.append(pokemon)

        filtered_pokemon = name_results

    # Filter by type.
    # This checks the Pokemon types list.
    # Example: Bulbasaur has ["Grass", "Poison"].

    if pokemon_type is not None:

        type_results = []

        for pokemon in filtered_pokemon:

            for single_type in pokemon.types:

                if single_type.lower() == pokemon_type.lower():
                    type_results.append(pokemon)

        filtered_pokemon = type_results

    # Filter by region.

    if region is not None:

        region_results = []

        for pokemon in filtered_pokemon:

            if pokemon.region.lower() == region.lower():
                region_results.append(pokemon)

        filtered_pokemon = region_results

    # Filter by generation.

    if generation is not None:

        generation_results = []

        for pokemon in filtered_pokemon:

            if pokemon.generation == generation:
                generation_results.append(pokemon)

        filtered_pokemon = generation_results

    # Filter by legendary status.

    if is_legendary is not None:

        legendary_results = []

        for pokemon in filtered_pokemon:

            if pokemon.is_legendary == is_legendary:
                legendary_results.append(pokemon)

        filtered_pokemon = legendary_results

    # Pagination happens after filtering.
    # This means count shows the number of matching Pokemon,
    # not just the total number in the full data list.

    paginated_pokemon = filtered_pokemon[offset: offset + limit]

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
        "count": len(filtered_pokemon),
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