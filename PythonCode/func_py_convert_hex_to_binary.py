# func_py_convert_hex_to_binary.py
def func_py_convert_hex_to_binary(hex_str):
    try:
        return bin(int(hex_str, 16))[2:]
    except ValueError:
        return None

print(func_py_convert_hex_to_binary('1A'))
print(func_py_convert_hex_to_binary('FF'))
