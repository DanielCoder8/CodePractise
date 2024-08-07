# func_py_generate_star_numbers.py
def func_py_generate_star_numbers(n):
    return [6 * i * (i - 1) + 1 for i in range(1, n+1)]

print(func_py_generate_star_numbers(10))
