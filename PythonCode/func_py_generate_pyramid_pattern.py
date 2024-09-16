# func_py_generate_pyramid_pattern.py
def func_py_generate_pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

func_py_generate_pyramid_pattern(5)
