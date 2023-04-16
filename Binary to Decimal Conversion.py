def binary_to_decimal(binary):
    """
    Converts a binary number to a decimal number.
    Args:
        binary (str): The binary number to convert.
    Returns:
        int: The decimal equivalent of the binary number.
    """
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    """
    Converts a decimal number to a binary number.
    Args:
        decimal (int): The decimal number to convert.
    Returns:
        str: The binary equivalent of the decimal number.
    """
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

binary_number = "101010"
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)

decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(binary_number)
