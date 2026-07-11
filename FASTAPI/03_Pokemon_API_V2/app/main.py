from fastapi import FastAPI

from app.routers import abilities, generations, pokemon, pokemon_types, regions


app = FastAPI(
    title="Pokemon API V2",
    description="A structured Pokemon API inspired by PokéAPI for learning FastAPI.",
    version="2.0.0",
)


app.include_router(pokemon.router)
app.include_router(pokemon_types.router)
app.include_router(regions.router)
app.include_router(abilities.router)
app.include_router(generations.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Pokemon API V2!",
        "api_info": "/api/v2",
        "docs": "/docs",
    }


@app.get("/api/v2")
def api_info():
    return {
        "name": "Pokemon API V2",
        "version": "2.0.0",
        "description": "A structured Pokemon API for learning FastAPI.",
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "pokemon": "/api/v2/pokemon",
            "pokemon_detail": "/api/v2/pokemon/{pokemon_identifier}",
            "pokemon_sprites": "/api/v2/pokemon/{pokemon_identifier}/sprites",
            "pokemon_stats": "/api/v2/pokemon/{pokemon_identifier}/stats",
            "types": "/api/v2/types",
            "type_detail": "/api/v2/types/{type_name}",
            "regions": "/api/v2/regions",
            "region_detail": "/api/v2/regions/{region_name}",
            "abilities": "/api/v2/abilities",
            "ability_detail": "/api/v2/abilities/{ability_name}",
            "generations": "/api/v2/generations",
            "generation_detail": "/api/v2/generations/{generation_number}",
        },
        "example_requests": [
            "/api/v2/pokemon",
            "/api/v2/pokemon?limit=20&offset=0",
            "/api/v2/pokemon?name=pika",
            "/api/v2/pokemon?type=Electric",
            "/api/v2/pokemon/pikachu",
            "/api/v2/pokemon/25",
            "/api/v2/pokemon/pikachu/sprites",
            "/api/v2/pokemon/pikachu/stats",
        ],
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Pokemon API V2 is running.",
    }