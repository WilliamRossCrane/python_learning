from flask import render_template, request
from app import app
from app.converters import (
    decimal_to_binary,
    binary_to_decimal,
    text_to_binary,
    check_rgb_value,
    rgb_to_hex,
    PIXEL_COLOURS,
    get_pixel_colour,
)


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


@app.route("/text-to-binary", methods=["GET", "POST"])
def text_binary_converter():
    text_value = None
    binary_result = None
    error = None

    if request.method == "POST":
        text_value = request.form.get("text_value", "").strip()

        try:
            binary_result = text_to_binary(text_value)
        except ValueError as message:
            error = message

    return render_template(
        "text_to_binary.html",
        text_value=text_value,
        binary_result=binary_result,
        error=error,
    )


@app.route("/rgb-lab", methods=["GET", "POST"])
def rgb_lab():
    red_value = 120
    green_value = 80
    blue_value = 200
    error = None

    if request.method == "POST":
        try:
            red_value = check_rgb_value(request.form.get("red_value", ""))
            green_value = check_rgb_value(request.form.get("green_value", ""))
            blue_value = check_rgb_value(request.form.get("blue_value", ""))
        except ValueError:
            error = "Please enter whole numbers between 0 and 255."

    rgb_value = f"rgb({red_value}, {green_value}, {blue_value})"
    hex_value = rgb_to_hex(red_value, green_value, blue_value)

    return render_template(
        "rgb_lab.html",
        red_value=red_value,
        green_value=green_value,
        blue_value=blue_value,
        rgb_value=rgb_value,
        hex_value=hex_value,
        error=error,
    )


@app.route("/pixel-beast", methods=["GET", "POST"])
def pixel_beast():
    default_pixels = [
        "white", "green", "white",
        "green", "black", "green",
        "white", "purple", "white",
    ]

    selected_pixels = default_pixels

    if request.method == "POST":
        selected_pixels = []

        for index in range(9):
            colour_name = request.form.get(f"pixel_{index}", "white")
            selected_pixels.append(colour_name)

    pixel_grid = []

    for index, colour_name in enumerate(selected_pixels):
        pixel_grid.append({
            "index": index,
            "name": colour_name,
            "hex": get_pixel_colour(colour_name),
        })

    return render_template(
        "pixel_beast.html",
        pixel_grid=pixel_grid,
        colour_options=PIXEL_COLOURS,
    )