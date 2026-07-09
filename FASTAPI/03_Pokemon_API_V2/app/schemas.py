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


# This is the smaller version used in the list route.
# Public APIs often return summaries first,
# then users can request the full detail route if needed.

class PokemonSummary(BaseModel):
    dex_number: int
    name: str
    slug: str
    types: list[str]
    detail_url: str


# This is the full response shape for the list route.
# It includes pagination information and a list of results.

class PokemonListResponse(BaseModel):
    count: int
    limit: int
    offset: int
    results: list[PokemonSummary]