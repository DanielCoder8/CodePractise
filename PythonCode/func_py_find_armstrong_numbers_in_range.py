# func_py_find_armstrong_numbers_in_range.py
def func_py_find_armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        num_str = str(num)
        if num == sum(int(digit) ** len(num_str) for digit in num_str):
            armstrong_numbers.append(num)
    return armstrong_numbers

print(func_py_find_armstrong_numbers_in_range(100, 999))
