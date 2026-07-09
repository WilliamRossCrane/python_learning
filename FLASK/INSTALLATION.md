````markdown
# Flask Installation

This guide shows how to install and run a Flask project.

Most Flask projects in this folder use a `requirements.txt` file.

A `requirements.txt` file lists the packages the project needs.

---

## 1. Move Into The Project Folder

From the main repo:

```bash
cd FLASK
```

Then move into the project you want to run.

Example:

```bash
cd CALCULATOR_V1_WEB
```

---

## 2. Create A Virtual Environment

```bash
python3 -m venv venv
```

A virtual environment keeps project packages separate from the rest of your computer.

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

Run:

```bash
pip install -r requirements.txt
```

This installs Flask and any other packages the project needs.

---

## 5. Run The Flask App

If the main file is called `app.py`, run:

```bash
flask --app app run --debug
```

If the main file is called `main.py`, run:

```bash
flask --app main run --debug
```

Some projects may have a different file name.

Use the project README if it gives a specific command.

---

## 6. Open The App

When Flask is running, open:

```text
http://127.0.0.1:5000
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

### `flask: command not found`

Activate the virtual environment:

```bash
source venv/bin/activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

---

### `ModuleNotFoundError`

This usually means the project packages are not installed.

Run:

```bash
pip install -r requirements.txt
```

---

### `No such file or directory: requirements.txt`

You may be in the wrong folder.

Check the current folder:

```bash
pwd
```

List the files:

```bash
ls
```

Move into the correct project folder and try again.

---

### The Website Does Not Load

Make sure the Flask server is running.

Then open:

```text
http://127.0.0.1:5000
```

---

## Notes

Use a virtual environment for each Flask project.

Use `pip install -r requirements.txt` when the project has a requirements file.

Use `Control + C` to stop the server.
````
