import argparse
import json
import time
from pathlib import Path

import requests


# This script gets Pokemon data from PokeAPI and saves it locally.
# It does not run every time the API starts.
# We run it manually when we want to refresh our local data.

API_BASE_URL = "https://pokeapi.co/api/v2"

# Where our cleaned Pokemon data will be saved.
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "app" / "data" / "pokemon.json"


GENERATION_NUMBERS = {
    "generation-i": 1,
    "generation-ii": 2,
    "generation-iii": 3,
    "generation-iv": 4,
    "generation-v": 5,
    "generation-vi": 6,
    "generation-vii": 7,
    "generation-viii": 8,
    "generation-ix": 9,
}


GENERATION_REGIONS = {
    "generation-i": "Kanto",
    "generation-ii": "Johto",
    "generation-iii": "Hoenn",
    "generation-iv": "Sinnoh",
    "generation-v": "Unova",
    "generation-vi": "Kalos",
    "generation-vii": "Alola",
    "generation-viii": "Galar",
    "generation-ix": "Paldea",
}


def get_json(url: str) -> dict:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.json()


def format_name(name: str) -> str:
    return name.replace("-", " ").title()


def get_stat_value(stats: list[dict], stat_name: str) -> int:
    for stat in stats:

        if stat["stat"]["name"] == stat_name:
            return stat["base_stat"]

    return 0


def clean_pokemon_data(pokemon_details: dict, species_details: dict) -> dict:
    dex_number = pokemon_details["id"]
    slug = pokemon_details["name"]
    name = format_name(slug)

    generation_name = species_details["generation"]["name"]

    types = []

    for pokemon_type in pokemon_details["types"]:
        type_name = pokemon_type["type"]["name"]
        types.append(format_name(type_name))

    abilities = []

    for ability_data in pokemon_details["abilities"]:
        ability_name = ability_data["ability"]["name"]
        abilities.append(format_name(ability_name))

    sprites = pokemon_details["sprites"]

    official_artwork = sprites["other"]["official-artwork"]["front_default"]

    description = (
        f"{name} is a {', '.join(types)} type Pokemon "
        f"from Generation {GENERATION_NUMBERS.get(generation_name, 0)}."
    )

    return {
        "id": dex_number,
        "dex_number": dex_number,
        "name": name,
        "slug": slug,
        "types": types,
        "abilities": abilities,
        "height_m": pokemon_details["height"] / 10,
        "weight_kg": pokemon_details["weight"] / 10,
        "region": GENERATION_REGIONS.get(generation_name, "Unknown"),
        "generation": GENERATION_NUMBERS.get(generation_name, 0),
        "description": description,
        "stats": {
            "hp": get_stat_value(pokemon_details["stats"], "hp"),
            "attack": get_stat_value(pokemon_details["stats"], "attack"),
            "defense": get_stat_value(pokemon_details["stats"], "defense"),
            "special_attack": get_stat_value(
                pokemon_details["stats"],
                "special-attack",
            ),
            "special_defense": get_stat_value(
                pokemon_details["stats"],
                "special-defense",
            ),
            "speed": get_stat_value(pokemon_details["stats"], "speed"),
        },
        "sprites": {
            "front_default": sprites["front_default"],
            "front_shiny": sprites["front_shiny"],
            "official_artwork": official_artwork,
        },
        "is_legendary": species_details["is_legendary"],
        "is_mythical": species_details["is_mythical"],
    }


def seed_pokemon(limit: int) -> None:
    print(f"Seeding the first {limit} Pokemon...")

    pokemon_data = []

    for pokemon_id in range(1, limit + 1):
        print(f"Fetching Pokemon {pokemon_id}...")

        pokemon_details = get_json(f"{API_BASE_URL}/pokemon/{pokemon_id}")
        species_details = get_json(f"{API_BASE_URL}/pokemon-species/{pokemon_id}")

        cleaned_pokemon = clean_pokemon_data(pokemon_details, species_details)

        pokemon_data.append(cleaned_pokemon)

        # Small pause so we are polite to the external API.
        time.sleep(0.05)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(pokemon_data, file, indent=2)

    print(f"Saved {len(pokemon_data)} Pokemon to:")
    print(OUTPUT_FILE)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seed local Pokemon data from PokeAPI."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=151,
        help="How many Pokemon to seed. Default is 151.",
    )

    args = parser.parse_args()

    seed_pokemon(limit=args.limit)


if __name__ == "__main__":
    main()