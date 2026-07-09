from pydantic import BaseModel, Field


class PokemonStats(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class PokemonSprites(BaseModel):
    front_default: str
    front_shiny: str | None = None
    official_artwork: str | None = None


class Pokemon(BaseModel):
    id: int
    dex_number: int
    name: str = Field(..., min_length=1, max_length=50)
    slug: str
    types: list[str]
    abilities: list[str]
    height_m: float
    weight_kg: float
    region: str
    generation: int
    description: str
    stats: PokemonStats
    sprites: PokemonSprites
    is_legendary: bool = False
    is_mythical: bool = False