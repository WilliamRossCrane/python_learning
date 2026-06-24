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


@app.route("/fox")
def fox():
    return render_template("fox.html")


@app.route("/treasure")
def treasure():
    return render_template("treasure.html")


@app.route("/game-over")
def game_over():
    return render_template("game_over.html")


@app.route("/victory")
def victory():
    return render_template("victory.html")