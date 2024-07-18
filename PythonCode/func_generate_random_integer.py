# func_generate_random_integer.py
import random

def func_generate_random_integer(start, end):
    return random.randint(start, end)

print(func_generate_random_integer(1, 100))
