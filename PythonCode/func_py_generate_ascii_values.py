# func_py_generate_ascii_values.py
def func_py_generate_ascii_values(s):
    return [ord(char) for char in s]

print(func_py_generate_ascii_values("hello"))
