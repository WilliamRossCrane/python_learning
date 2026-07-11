from fastapi import FastAPI

from app.routers import pokemon, pokemon_types


app = FastAPI(
    title="Pokemon API V2",
    description="A structured Pokemon API inspired by PokéAPI for learning FastAPI.",
    version="2.0.0",
)


app.include_router(pokemon.router)
app.include_router(pokemon_types.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Pokemon API V2!",
        "docs": "/docs",
        "pokemon": "/api/v2/pokemon",
        "types": "/api/v2/types",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Pokemon API V2 is running.",
    }