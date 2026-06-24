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