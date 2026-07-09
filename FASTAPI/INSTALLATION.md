````markdown
# FastAPI Installation

This guide shows how to install and run a FastAPI project.

---

## 1. Move Into The Project Folder

From the main repo:

```bash
cd FASTAPI/01_Rest_API
```
````

---

## 2. Create A Virtual Environment

```bash
python3 -m venv venv
```

---

## 3. Activate The Virtual Environment

On Mac:

```bash
source venv/bin/activate
```

You should see:

```text
(venv)
```

at the start of your terminal line.

---

## 4. Install Requirements

If the project has a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file yet, install FastAPI with:

```bash
pip install "fastapi[standard]"
```

---

## 5. Run The FastAPI Server

If the file is called `main.py` and the app variable is called `app`, run:

```bash
uvicorn main:app --reload
```

This starts the API at:

```text
http://127.0.0.1:8000
```

---

## 6. Open The API Docs

FastAPI creates a testing page automatically.

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 7. Stop The Server

Press:

```text
Control + C
```

---

## 8. Deactivate The Virtual Environment

When finished, run:

```bash
deactivate
```

---

## Common Issues

### `uvicorn: command not found`

Activate the virtual environment:

```bash
source venv/bin/activate
```

Then install requirements again:

```bash
pip install -r requirements.txt
```

---

### `ModuleNotFoundError: No module named fastapi`

FastAPI is not installed.

Run:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install "fastapi[standard]"
```

---

### `Error loading ASGI app`

Check that:

- you are in the correct folder
- the file is called `main.py`
- the FastAPI app variable is called `app`

Run:

```bash
uvicorn main:app --reload
```

---

## Notes

Use `uvicorn main:app --reload` whenever you want to run the FastAPI project locally.

```

```
