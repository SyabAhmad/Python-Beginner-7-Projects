import random
import string

def generate_password(length):
    """
    Generates a random password of specified length.
    Args:
        length (int): The length of the password to generate.
    Returns:
        str: The random password.
    """
    # Define the character sets to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine the character sets into one set of characters to choose from
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate the password by randomly selecting characters from the set
    password = "".join(random.choices(all_characters, k=length))

    return password


print(generate_password(7))