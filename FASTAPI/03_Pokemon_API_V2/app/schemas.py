from pydantic import BaseModel, Field


# These models describe the data that the API returns.
# They help FastAPI turn Python objects into JSON in a clear way.


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


# This smaller model is used for list views.
# It gives a short summary instead of the full Pokemon details.
class PokemonSummary(BaseModel):
    dex_number: int
    name: str
    slug: str
    types: list[str]
    detail_url: str


# This model describes the response for the main Pokemon list route.
class PokemonListResponse(BaseModel):
    count: int
    next: str | None = None
    previous: str | None = None
    limit: int
    offset: int
    results: list[PokemonSummary]


class PokemonTypeListResponse(BaseModel):
    count: int
    results: list[str]


class PokemonTypeDetailResponse(BaseModel):
    name: str
    pokemon_count: int
    pokemon: list[PokemonSummary]


class RegionListResponse(BaseModel):
    count: int
    results: list[str]


class RegionDetailResponse(BaseModel):
    name: str
    pokemon_count: int
    pokemon: list[PokemonSummary]


class AbilityListResponse(BaseModel):
    count: int
    results: list[str]


class AbilityDetailResponse(BaseModel):
    name: str
    pokemon_count: int
    pokemon: list[PokemonSummary]


class GenerationListResponse(BaseModel):
    count: int
    results: list[int]


class GenerationDetailResponse(BaseModel):
    generation: int
    pokemon_count: int
    pokemon: list[PokemonSummary]


class PokemonSpriteResponse(BaseModel):
    dex_number: int
    name: str
    slug: str
    sprites: PokemonSprites


class PokemonStatsResponse(BaseModel):
    dex_number: int
    name: str
    slug: str
    stats: PokemonStats
    base_stat_total: int


class APIStatsResponse(BaseModel):
    total_pokemon: int
    total_types: int
    total_regions: int
    total_abilities: int
    total_generations: int
    legendary_count: int
    mythical_count: int