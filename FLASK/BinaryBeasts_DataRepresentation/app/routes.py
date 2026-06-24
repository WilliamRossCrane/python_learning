from flask import render_template, request
from app import app
from app.converters import decimal_to_binary, binary_to_decimal


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/binary-converter", methods=["GET", "POST"])
def binary_converter():
    binary_result = None
    decimal_number = None
    error = None

    if request.method == "POST":
        user_input = request.form.get("decimal_number", "").strip()

        if user_input == "":
            error = "Please enter a whole number."
        else:
            try:
                decimal_number = int(user_input)
                binary_result = decimal_to_binary(decimal_number)
            except ValueError:
                error = "Please enter a zero or positive whole number."

    return render_template(
        "binary_converter.html",
        decimal_number=decimal_number,
        binary_result=binary_result,
        error=error,
    )


@app.route("/decimal-converter", methods=["GET", "POST"])
def decimal_converter():
    decimal_result = None
    binary_value = None
    error = None

    if request.method == "POST":
        binary_value = request.form.get("binary_value", "").strip()

        try:
            decimal_result = binary_to_decimal(binary_value)
        except ValueError as message:
            error = message

    return render_template(
        "decimal_converter.html",
        binary_value=binary_value,
        decimal_result=decimal_result,
        error=error,
    )