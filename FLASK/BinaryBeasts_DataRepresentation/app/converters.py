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