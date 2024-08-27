# func_py_find_pronic_numbers.py
def func_py_find_pronic_numbers(limit):
    return [n * (n + 1) for n in range(1, limit)]

print(func_py_find_pronic_numbers(20))
