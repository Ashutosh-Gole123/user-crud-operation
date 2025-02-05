import random
import string

def generate_temp_password(length=8):
    """
    Generate a random temporary password.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
