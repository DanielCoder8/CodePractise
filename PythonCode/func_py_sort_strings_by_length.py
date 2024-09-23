# func_py_sort_strings_by_length.py
def func_py_sort_strings_by_length(strings):
    return sorted(strings, key=len)

print(func_py_sort_strings_by_length(["apple", "banana", "cherry", "kiwi"]))
