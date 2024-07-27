# func_py_generate_random_string.py
import random
import string

def func_py_generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

print(func_py_generate_random_string(10))
