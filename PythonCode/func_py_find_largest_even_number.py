# func_py_find_largest_even_number.py
def func_py_find_largest_even_number(lst):
    evens = [num for num in lst if num % 2 == 0]
    return max(evens) if evens else None

print(func_py_find_largest_even_number([1, 2, 5, 6, 10]))
