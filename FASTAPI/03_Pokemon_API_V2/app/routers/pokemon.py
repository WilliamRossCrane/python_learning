from fastapi import APIRouter, HTTPException, Query, Request

from app.data.pokemon_data import pokemon_list
from app.schemas import (
    Pokemon,
    PokemonListResponse,
    PokemonSpriteResponse,
    PokemonStatsResponse,
    PokemonSummary,
)


router = APIRouter(
    prefix="/api/v2",
    tags=["Pokemon"],
)


# This helper function finds one Pokemon by dex number or slug.
# Example:
# 1 = Bulbasaur
# bulbasaur = Bulbasaur

def find_pokemon_by_identifier(pokemon_identifier: str) -> Pokemon | None:

    for pokemon in pokemon_list:

        if str(pokemon.dex_number) == pokemon_identifier:
            return pokemon

        if pokemon.slug.lower() == pokemon_identifier.lower():
            return pokemon

    return None


# This route returns a paginated list of Pokemon summaries.
# It can also search and filter Pokemon using query parameters.
#
# Examples:
# /api/v2/pokemon
# /api/v2/pokemon?limit=20&offset=0
# /api/v2/pokemon?name=char
# /api/v2/pokemon?type=Fire
# /api/v2/pokemon?region=Kanto
# /api/v2/pokemon?generation=1
# /api/v2/pokemon?is_legendary=true

@router.get("/pokemon", response_model=PokemonListResponse)
def get_all_pokemon(
    request: Request,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    name: str | None = None,
    pokemon_type: str | None = Query(default=None, alias="type"),
    region: str | None = None,
    generation: int | None = None,
    is_legendary: bool | None = None,
):

    filtered_pokemon = pokemon_list

    if name is not None:

        name_results = []

        for pokemon in filtered_pokemon:

            if name.lower() in pokemon.name.lower():
                name_results.append(pokemon)

        filtered_pokemon = name_results

    if pokemon_type is not None:

        type_results = []

        for pokemon in filtered_pokemon:

            for single_type in pokemon.types:

                if single_type.lower() == pokemon_type.lower():
                    type_results.append(pokemon)

        filtered_pokemon = type_results

    if region is not None:

        region_results = []

        for pokemon in filtered_pokemon:

            if pokemon.region.lower() == region.lower():
                region_results.append(pokemon)

        filtered_pokemon = region_results

    if generation is not None:

        generation_results = []

        for pokemon in filtered_pokemon:

            if pokemon.generation == generation:
                generation_results.append(pokemon)

        filtered_pokemon = generation_results

    if is_legendary is not None:

        legendary_results = []

        for pokemon in filtered_pokemon:

            if pokemon.is_legendary == is_legendary:
                legendary_results.append(pokemon)

        filtered_pokemon = legendary_results

    total_count = len(filtered_pokemon)

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

    next_url = None
    previous_url = None

    if offset + limit < total_count:
        next_url = str(
            request.url.include_query_params(
                limit=limit,
                offset=offset + limit,
            )
        )

    if offset > 0:
        previous_offset = max(offset - limit, 0)

        previous_url = str(
            request.url.include_query_params(
                limit=limit,
                offset=previous_offset,
            )
        )

    return {
        "count": total_count,
        "next": next_url,
        "previous": previous_url,
        "limit": limit,
        "offset": offset,
        "results": results,
    }


# This route returns only sprite data for one Pokemon.
# This is useful for apps that only need image URLs.

@router.get("/pokemon/{pokemon_identifier}/sprites", response_model=PokemonSpriteResponse)
def get_pokemon_sprites(pokemon_identifier: str):

    pokemon = find_pokemon_by_identifier(pokemon_identifier)

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return {
        "dex_number": pokemon.dex_number,
        "name": pokemon.name,
        "slug": pokemon.slug,
        "sprites": pokemon.sprites,
    }


# This route returns only stat data for one Pokemon.
# It also calculates the base stat total.
# This is useful for apps that compare Pokemon strength.

@router.get("/pokemon/{pokemon_identifier}/stats", response_model=PokemonStatsResponse)
def get_pokemon_stats(pokemon_identifier: str):

    pokemon = find_pokemon_by_identifier(pokemon_identifier)

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    base_stat_total = (
        pokemon.stats.hp
        + pokemon.stats.attack
        + pokemon.stats.defense
        + pokemon.stats.special_attack
        + pokemon.stats.special_defense
        + pokemon.stats.speed
    )

    return {
        "dex_number": pokemon.dex_number,
        "name": pokemon.name,
        "slug": pokemon.slug,
        "stats": pokemon.stats,
        "base_stat_total": base_stat_total,
    }


# This route returns the full data for one Pokemon.
# The user can search by dex number or slug.

@router.get("/pokemon/{pokemon_identifier}", response_model=Pokemon)
def get_pokemon(pokemon_identifier: str):

    pokemon = find_pokemon_by_identifier(pokemon_identifier)

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return pokemon