def decimal_to_binary(decimal_number):
    """
    Convert a decimal number into binary.

    Decimal is the normal number system we use every day.
    Binary is the number system computers use, made from 0s and 1s.
    """
    if decimal_number < 0:
        raise ValueError("Only zero or positive whole numbers can be converted.")

    return bin(decimal_number)[2:]

def binary_to_decimal(binary_string):
    """
    Convert a binary string into a decimal number.

    Binary only uses 0 and 1.
    Decimal is the normal number system humans usually use.
    """
    if binary_string == "":
        raise ValueError("Binary value cannot be empty.")

    for digit in binary_string:
        if digit not in ["0", "1"]:
            raise ValueError("Binary values can only contain 0 and 1.")

    return int(binary_string, 2)

def text_to_binary(text):
    """
    Convert text into binary.

    Each character is turned into a number using ord().
    That number is then converted into an 8-bit binary value.
    """
    if text == "":
        raise ValueError("Text cannot be empty.")

    binary_letters = []

    for character in text:
        binary_value = format(ord(character), "08b")
        binary_letters.append(binary_value)

    return " ".join(binary_letters)

def check_rgb_value(value):
    """
    Check that an RGB value is a whole number between 0 and 255.
    """
    number = int(value)

    if number < 0 or number > 255:
        raise ValueError("RGB values must be between 0 and 255.")

    return number


def rgb_to_hex(red, green, blue):
    """
    Convert RGB values into a hexadecimal colour code.

    Example:
    Red 255, Green 0, Blue 0 becomes #FF0000.
    """
    return f"#{red:02X}{green:02X}{blue:02X}"

PIXEL_COLOURS = {
    "black": "#111827",
    "white": "#F9FAFB",
    "green": "#22C55E",
    "blue": "#3B82F6",
    "purple": "#A855F7",
    "yellow": "#FACC15",
    "red": "#EF4444",
}


def get_pixel_colour(colour_name):
    """
    Return the hex colour code for a pixel colour name.

    If the colour is not found, return white as a safe default.
    """
    return PIXEL_COLOURS.get(colour_name, "#F9FAFB")