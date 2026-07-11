from fastapi import APIRouter, HTTPException

from app.data.pokemon_data import pokemon_list
from app.schemas import (
    PokemonSummary,
    RegionDetailResponse,
    RegionListResponse,
)


router = APIRouter(
    prefix="/api/v2",
    tags=["Regions"],
)


# This route returns every region that appears in the data.
@router.get("/regions", response_model=RegionListResponse)
def get_all_regions():
    regions = []

    for pokemon in pokemon_list:
        if pokemon.region not in regions:
            regions.append(pokemon.region)

    regions.sort()

    return {
        "count": len(regions),
        "results": regions,
    }


# This route returns all Pokemon from one region.
@router.get("/regions/{region_name}", response_model=RegionDetailResponse)
def get_region_details(region_name: str):
    matching_pokemon = []
    matched_region_name = None

    for pokemon in pokemon_list:
        if pokemon.region.lower() == region_name.lower():
            matched_region_name = pokemon.region

            pokemon_summary = PokemonSummary(
                dex_number=pokemon.dex_number,
                name=pokemon.name,
                slug=pokemon.slug,
                types=pokemon.types,
                detail_url=f"/api/v2/pokemon/{pokemon.slug}",
            )

            matching_pokemon.append(pokemon_summary)

    if matched_region_name is None:
        raise HTTPException(status_code=404, detail="Pokemon region not found")

    return {
        "name": matched_region_name,
        "pokemon_count": len(matching_pokemon),
        "pokemon": matching_pokemon,
    }