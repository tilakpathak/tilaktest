import random
import string

def generate_random_email():
    """Generate a random email address."""
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "example.com"
    return f"{local_part}@{domain}"

def generate_random_password(length=8):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
