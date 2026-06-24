def decimal_to_binary(decimal_number):
    """
    Convert a decimal number into binary.

    Decimal is the normal number system we use every day.
    Binary is the number system computers use, made from 0s and 1s.
    """
    if decimal_number < 0:
        raise ValueError("Only zero or positive whole numbers can be converted.")

    return bin(decimal_number)[2:]