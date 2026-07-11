from fastapi import APIRouter

from app.data.pokemon_data import pokemon_list
from app.schemas import APIStatsResponse


router = APIRouter(
    prefix="/api/v2",
    tags=["API Stats"],
)


# This route returns summary information about the whole API dataset.
# It is useful for apps that want a quick overview of the data.

@router.get("/stats", response_model=APIStatsResponse)
def get_api_stats():

    types = []
    regions = []
    abilities = []
    generations = []

    legendary_count = 0
    mythical_count = 0

    for pokemon in pokemon_list:

        for single_type in pokemon.types:

            if single_type not in types:
                types.append(single_type)

        if pokemon.region not in regions:
            regions.append(pokemon.region)

        for ability in pokemon.abilities:

            if ability not in abilities:
                abilities.append(ability)

        if pokemon.generation not in generations:
            generations.append(pokemon.generation)

        if pokemon.is_legendary:
            legendary_count += 1

        if pokemon.is_mythical:
            mythical_count += 1

    return {
        "total_pokemon": len(pokemon_list),
        "total_types": len(types),
        "total_regions": len(regions),
        "total_abilities": len(abilities),
        "total_generations": len(generations),
        "legendary_count": legendary_count,
        "mythical_count": mythical_count,
    }