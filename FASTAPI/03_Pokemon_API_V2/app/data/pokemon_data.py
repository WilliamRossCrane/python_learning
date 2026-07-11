import json
from pathlib import Path

from app.schemas import Pokemon


# This file loads Pokemon data from pokemon.json.
# The seed script creates pokemon.json.
# The API then reads from that local file.

DATA_FILE = Path(__file__).resolve().parent / "pokemon.json"


def load_pokemon_data() -> list[Pokemon]:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        raw_pokemon_data = json.load(file)

    pokemon_list = []

    for single_pokemon in raw_pokemon_data:
        pokemon = Pokemon(**single_pokemon)
        pokemon_list.append(pokemon)

    return pokemon_list


pokemon_list: list[Pokemon] = load_pokemon_data()