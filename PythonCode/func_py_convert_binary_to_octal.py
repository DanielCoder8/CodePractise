# func_py_convert_binary_to_octal.py
def func_py_convert_binary_to_octal(binary_str):
    try:
        return oct(int(binary_str, 2))[2:]
    except ValueError:
        return None

print(func_py_convert_binary_to_octal('1010'))
print(func_py_convert_binary_to_octal('1111'))
