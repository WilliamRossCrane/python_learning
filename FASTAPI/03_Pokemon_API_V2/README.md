# Pokemon API V2

This project is a beginner-friendly FastAPI API for learning about:

- REST API routes
- JSON responses
- query parameters
- routers and schemas
- seeding local data

## Run the app

From the project folder, start the API with:

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

Then open the docs at:

- http://127.0.0.1:8000/docs

## Main routes

- GET /api/v2
- GET /api/v2/stats
- GET /api/v2/pokemon
- GET /api/v2/pokemon?limit=20&offset=0
- GET /api/v2/pokemon/random
- GET /api/v2/pokemon/pikachu
- GET /api/v2/pokemon/pikachu/sprites
- GET /api/v2/pokemon/pikachu/stats
- GET /api/v2/types
- GET /api/v2/regions
- GET /api/v2/abilities
- GET /api/v2/generations

## Seed the data

The seed script downloads Pokemon data from PokéAPI and saves it to a local JSON file.
This keeps the learning API simple and quick to use.

```bash
python scripts/seed_pokemon.py --limit 151
```
