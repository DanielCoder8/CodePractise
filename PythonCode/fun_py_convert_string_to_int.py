# fun_py_convert_string_to_int.py
def fun_py_convert_string_to_int(string):
    try:
        return int(string)
    except ValueError:
        return None

print(fun_py_convert_string_to_int("12345"))
print(fun_py_convert_string_to_int("abc"))
