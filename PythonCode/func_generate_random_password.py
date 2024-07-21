# func_generate_random_password.py
import random
import string

def func_generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print(func_generate_random_password(12))
