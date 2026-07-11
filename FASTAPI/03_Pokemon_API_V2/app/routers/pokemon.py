import random

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


# This helper can find one Pokemon by its dex number or its slug.
# Example: 25 or pikachu both work.
def find_pokemon_by_identifier(pokemon_identifier: str) -> Pokemon | None:
    for pokemon in pokemon_list:
        if str(pokemon.dex_number) == pokemon_identifier:
            return pokemon

        if pokemon.slug.lower() == pokemon_identifier.lower():
            return pokemon

    return None


# This route returns a list of Pokemon with optional filters and pagination.
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
    paginated_pokemon = filtered_pokemon[offset : offset + limit]

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


# This route returns one random Pokemon for a fun demo.
@router.get("/pokemon/random", response_model=Pokemon)
def get_random_pokemon():
    if len(pokemon_list) == 0:
        raise HTTPException(status_code=404, detail="No Pokemon data found")

    random_pokemon = random.choice(pokemon_list)

    return random_pokemon


# This route returns only the sprite links for one Pokemon.
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


# This route returns the base stats for one Pokemon.
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


# This route returns the full details for one Pokemon.
@router.get("/pokemon/{pokemon_identifier}", response_model=Pokemon)
def get_pokemon(pokemon_identifier: str):
    pokemon = find_pokemon_by_identifier(pokemon_identifier)

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    return pokemon