# func_py_remove_duplicates_from_list.py
def func_py_remove_duplicates_from_list(lst):
    return list(dict.fromkeys(lst))

print(func_py_remove_duplicates_from_list([1, 2, 2, 3, 4, 4, 5]))
