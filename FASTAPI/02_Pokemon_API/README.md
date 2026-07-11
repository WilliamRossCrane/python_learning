# 02 Pokemon API

This is a beginner FastAPI project.

The goal is to build a small Pokemon API step by step while learning how REST APIs work.

This project uses temporary in-memory data, which means the Pokemon list resets when the server restarts.

---

## What This Project Teaches

- FastAPI basics
- REST API routes
- JSON responses
- path parameters
- query parameters
- request bodies
- Pydantic models
- validation rules
- enum choices
- CRUD actions
- simple helper functions
- calculated API data

---

## Key API Ideas

| Concept         | Meaning                                                |
| --------------- | ------------------------------------------------------ |
| `GET`           | Read data                                              |
| `POST`          | Create new data                                        |
| `PUT`           | Update existing data                                   |
| `DELETE`        | Remove data                                            |
| Path parameter  | A value inside the URL, like `/pokemon/1`              |
| Query parameter | A filter in the URL, like `/pokemon?pokemon_type=Fire` |
| Request body    | JSON data sent to the API                              |
| Response body   | JSON data returned by the API                          |
| Model           | A structure that describes what data should look like  |
| Validation      | Rules that stop bad data from being accepted           |
| Enum            | A set list of allowed choices                          |

---

## Run The API

Move into the project folder:

```bash
cd FASTAPI/02_Pokemon_API
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open the API:

```text
http://127.0.0.1:8000
```

Open the interactive docs:

```text
http://127.0.0.1:8000/docs
```

Stop the server:

```text
Control + C
```

Deactivate the virtual environment:

```bash
deactivate
```

---

## Current Routes

| Method   | Route                                          | What It Does                         |
| -------- | ---------------------------------------------- | ------------------------------------ |
| `GET`    | `/`                                            | Shows a welcome message              |
| `GET`    | `/health`                                      | Checks if the API is running         |
| `GET`    | `/pokemon`                                     | Returns all Pokemon                  |
| `GET`    | `/pokemon?pokemon_type=Fire`                   | Filters Pokemon by type              |
| `GET`    | `/pokemon?pokemon_name=char`                   | Searches Pokemon by name             |
| `GET`    | `/pokemon?pokemon_type=Fire&pokemon_name=char` | Filters by type and searches by name |
| `GET`    | `/pokemon/stats`                               | Returns Pokemon stats                |
| `GET`    | `/pokemon/types`                               | Returns available Pokemon types      |
| `GET`    | `/pokemon/{pokemon_id}`                        | Returns one Pokemon by ID            |
| `POST`   | `/pokemon`                                     | Creates a new Pokemon                |
| `PUT`    | `/pokemon/{pokemon_id}`                        | Updates a Pokemon                    |
| `DELETE` | `/pokemon/{pokemon_id}`                        | Deletes a Pokemon                    |

---

## Example Pokemon Data

Each Pokemon returned by the API has:

```json
{
  "id": 1,
  "name": "Bulbasaur",
  "type": "Grass",
  "level": 5
}
```

The `id` is created by the API.

When creating or updating a Pokemon, the user sends:

```json
{
  "name": "Pikachu",
  "type": "Electric",
  "level": 7
}
```

---

## Test The API With Curl

Get all Pokemon:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon"
```

Get one Pokemon by ID:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon/1"
```

Filter Pokemon by type:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon?pokemon_type=Fire"
```

Search Pokemon by name:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon?pokemon_name=char"
```

Filter and search together:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon?pokemon_type=Fire&pokemon_name=char"
```

Get Pokemon stats:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon/stats"
```

Get available Pokemon types:

```bash
curl -X GET "http://127.0.0.1:8000/pokemon/types"
```

Create a Pokemon:

```bash
curl -X POST "http://127.0.0.1:8000/pokemon" \
     -H "Content-Type: application/json" \
     -d '{"name": "Pikachu", "type": "Electric", "level": 7}'
```

Update a Pokemon:

```bash
curl -X PUT "http://127.0.0.1:8000/pokemon/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Ivysaur", "type": "Grass", "level": 16}'
```

Delete a Pokemon:

```bash
curl -X DELETE "http://127.0.0.1:8000/pokemon/1"
```

---

## Validation Rules

The API checks that Pokemon data makes sense.

| Field   | Rule                                     |
| ------- | ---------------------------------------- |
| `name`  | Required, 1 to 30 characters             |
| `type`  | Must be one of the allowed Pokemon types |
| `level` | Must be between 1 and 100                |

Invalid example:

```json
{
  "name": "",
  "type": "Banana",
  "level": 999
}
```

This should fail because:

- the name is empty
- Banana is not an allowed type
- the level is too high

---

## Available Pokemon Types

The API currently allows:

- Grass
- Fire
- Water
- Electric
- Normal
- Psychic

These are controlled by an enum in `main.py`.

---

## How The Data Works

This project stores Pokemon in a Python list.

That means the data is temporary.

If the server restarts, any Pokemon created while the server was running will disappear.

This is normal for a beginner API project.

Later, this could be upgraded to use:

- a JSON file
- SQLite
- a database with SQLAlchemy

---

## Student Challenges

Try adding these features:

1. Add more Pokemon to the starter list.
2. Add more Pokemon types to the enum.
3. Add a route that returns only high-level Pokemon.
4. Add a route that levels up a Pokemon by 1.
5. Add an `is_legendary` field.
6. Add a `region` field.
7. Add a route that filters Pokemon by minimum level.
8. Add a route that returns a random Pokemon.
9. Add a second type field, like `secondary_type`.
10. Save the Pokemon data to a JSON file.

---

## Learning Reflection

After finishing this project, students should be able to explain:

- what an API is
- what JSON is
- how FastAPI routes work
- how path parameters work
- how query parameters work
- how request bodies work
- why validation matters
- what an enum is
- how CRUD actions work
- why APIs need clear and consistent data

---

## Next Steps

This project currently stores data in a Python list.

A more advanced version could use:

- a JSON file
- SQLite
- SQLAlchemy
- separate files for routes, models, and data
- automated tests
- a small frontend
