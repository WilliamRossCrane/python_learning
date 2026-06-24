from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/forest")
def forest():
    return render_template("forest.html")


@app.route("/cave")
def cave():
    return render_template("cave.html")