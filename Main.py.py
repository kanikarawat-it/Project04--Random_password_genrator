import random
import string
def generate_password(length=12):
    # Define character set (lowercase, uppercase, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by choosing characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Generate a random password of 12 characters
print(generate_password(12))
