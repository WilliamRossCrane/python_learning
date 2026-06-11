from flask import render_template, request
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        result = "Invalid operation"

    return render_template("index.html", result=result)