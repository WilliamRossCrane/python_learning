from fastapi import FastAPI

from app.routers import abilities, pokemon, pokemon_types, regions


app = FastAPI(
    title="Pokemon API V2",
    description="A structured Pokemon API inspired by PokéAPI for learning FastAPI.",
    version="2.0.0",
)


app.include_router(pokemon.router)
app.include_router(pokemon_types.router)
app.include_router(regions.router)
app.include_router(abilities.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Pokemon API V2!",
        "docs": "/docs",
        "pokemon": "/api/v2/pokemon",
        "types": "/api/v2/types",
        "regions": "/api/v2/regions",
        "abilities": "/api/v2/abilities",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Pokemon API V2 is running.",
    }