# func_py_generate_pronic_numbers.py
def func_py_generate_pronic_numbers(limit):
    pronic_numbers = [n * (n + 1) for n in range(1, limit + 1)]
    return pronic_numbers

print(func_py_generate_pronic_numbers(10))
