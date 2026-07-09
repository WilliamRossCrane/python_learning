````markdown
# Python Fundamentals Installation

The Python Fundamentals projects only use basic Python files.

You do not need:

- Flask
- FastAPI
- a virtual environment
- `requirements.txt`
- extra packages

You only need Python installed.

---

## 1. Check Python Is Installed

Open the terminal and run:

```bash
python3 --version
```

You should see something like:

```text
Python 3.12.0
```

The version number may be different. That is okay.

---

## 2. Move Into A Project Folder

From the main repo, move into a Fundamentals project.

Example:

```bash
cd FUNDAMENTALS/01_hello_python
```

---

## 3. Run The Python File

Most projects use:

```text
main.py
```

Run the file with:

```bash
python3 main.py
```

---

## Example

```bash
cd FUNDAMENTALS/01_hello_python
python3 main.py
```

---

## 4. Stop A Program

Most beginner programs finish by themselves.

If a program keeps running, press:

```text
Control + C
```

---

## Common Issues

### `python3: command not found`

Python may not be installed.

Install Python, then try again.

---

### `No such file or directory`

You may be in the wrong folder.

Check where you are:

```bash
pwd
```

List the files in the current folder:

```bash
ls
```

Move into the correct project folder and try again.

---

### `can't open file 'main.py'`

You are probably not inside the project folder.

Make sure the folder contains:

```text
main.py
```

You can check with:

```bash
ls
```

---

## Notes

Fundamentals projects are simple Python practice.

Use:

```bash
python3 main.py
```

to run each project.
````
