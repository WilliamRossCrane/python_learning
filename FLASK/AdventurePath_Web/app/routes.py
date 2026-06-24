from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("start.html")