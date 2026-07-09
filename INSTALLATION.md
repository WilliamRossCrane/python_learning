````markdown
# Installation Guide

This guide helps you set up the basic tools needed for this Python learning repo.

You only need to install:

- Python
- VS Code
- Git

Flask and FastAPI setup is explained inside their own folders.

---

## 1. Install Python

Download Python from:

```text
https://www.python.org/downloads/
```

Install the latest version for your computer.

After installing Python, open the terminal and check it works:

```bash
python3 --version
```

You should see something like:

```text
Python 3.12.0
```

The version number may be different. That is okay.

---

## 2. Install VS Code

Download Visual Studio Code from:

```text
https://code.visualstudio.com/
```

VS Code is the editor used to open and write the code.

---

## 3. Install Git

Download Git from:

```text
https://git-scm.com/downloads
```

After installing Git, check it works:

```bash
git --version
```

You should see something like:

```text
git version 2.x.x
```

---

## 4. Open The Project

Open VS Code.

Go to:

```text
File > Open Folder
```

Choose the main project folder:

```text
python_learning
```

---

## 5. Open The Terminal

In VS Code, open a terminal:

```text
Terminal > New Terminal
```

The terminal is where you run commands.

---

## Basic Terminal Commands

Show the folder you are currently in:

```bash
pwd
```

Show the files and folders in the current location:

```bash
ls
```

Move into a folder:

```bash
cd folder_name
```

Move back one folder:

```bash
cd ..
```

Stop a running program:

```text
Control + C
```

---

## Basic Git Commands

Check the current Git status:

```bash
git status
```

Add changed files:

```bash
git add .
```

Save changes with a commit:

```bash
git commit -m "Your commit message"
```

Check recent commits:

```bash
git log --oneline
```

---

## Notes

This top-level guide is only for the basic setup.

For specific project setup, use the installation guide inside each folder:

```text
FUNDAMENTALS/INSTALLATION.md
FLASK/INSTALLATION.md
FASTAPI/INSTALLATION.md
```
````
